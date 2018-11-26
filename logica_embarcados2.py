# Declarao bibliotecas
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
import RPi.GPIO as GPIO
import time

class eletronica:

    servidor = ''

    def upadte_server_value(new_value):
        servidor = new_value
        print('valor do servidor' + str(servidor))
        update_door_state(servidor)


    def update_door_state(servidor):

        #DISPLAY



        #------------------------------------------------------
        #   PROGRAMA PRINCIPAL Display Oled com Raspberry Pi
        #------------------------------------------------------
        #Variaveis globais
        # Raspberry Pi - configuracao dos pinos:
        RST = 24 #embora nao utilizado de fato, eh preciso defini-lo para a biblioteca funcionar

        # Configura uso do display OLED de 128x64 (comunicacao I²C)
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        #Inicializa biblioteca de comunicacao com display e o limpa
        disp.begin()
        disp.clear()
        disp.display()

        #obtem altura e largura totais do display
        width = disp.width
        height = disp.height

        #Carregamento das imagens.
        #Importante: quanto maior a imagem, mais tempo esta conversao levara.

        #Carrega a imagem 1 (ImagemTeste1.png) e automaticamente ja binariza e ajusta a resolução da mesma.
        image1 = Image.open('Imagem1.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

        #Carrega a imagem 2 (ImagemTeste2.png) e automaticamente ja binariza e ajusta a resolução da mesma.
        image2 = Image.open('Imagem2.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

        #Carrega a imagem 2 (ImagemTeste2.png) e automaticamente ja binariza e ajusta a resolução da mesma.
        image3 = Image.open('Imagem3.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')



        #Conexo dos sensores fim de curso no pino 3Vcc da Raspberry e retoro no pinos indicados abaixo:
        BtnPin1 = 25    # Fim_curso1
        BtnPin2 = 23    # Fim_curso2

        #Rele:
        Rele = 18      # Acionamento do Rele (Pino IN no rele), 5Vcc e Gnd da raspeberry.

        #Sensores LDR:
        Sensor = 24     # Conexo do pino de saida do CI Logico OR, conexo dos 3 sensores LDR.

        #Comando do servidor: 0 (Liberar) ou 1 (bloquear)
        servidor = 1

        #Rele:
        Buzzer = 17       # Acionamento do Rele (Pino IN no rele), 5Vcc e Gnd da raspeberry.

        #motor
        MOTORD = 27
        MOTORE = 22

        #Configurar Pinos:
        GPIO.setmode(GPIO.BCM)


        GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(BtnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Sensor, GPIO.IN)

        #Aciona o Relay
        GPIO.setup(Rele, GPIO.OUT)

        #aciona o buzzer
        GPIO.setup(17, GPIO.OUT)

        #motor
        GPIO.setup(MOTORD, GPIO.OUT)
        GPIO.setup(MOTORE, GPIO.OUT)


                #Mostra a imagem 1 por 5 segundos
                #disp.image(image3)
                #disp.display()
                #time.sleep(0.1)

        #inicio do programa
        try:
            while True:
        #



                #buzzer
                #GPIO.output(17,False)
                print(GPIO.input(Sensor))
                print(GPIO.input(BtnPin1))
                print(GPIO.input(BtnPin2))
                print(GPIO.input(MOTORD))
                print(GPIO.input(MOTORE))


        #Condes de Operao:
        #Grupo 1:
                if (servidor == 0 or servidor == 1) and (GPIO.input(Sensor) == False) and (GPIO.input(BtnPin1) == False and GPIO.input(BtnPin2) == False): # Sensores no acionado e a porta em movimento
                    #Emiti mensagem no Display
                    print('Porta em movimento')
                    disp.image(image3)
                    disp.display()
                    time.sleep(0.1)

        	    # Buzzer desligado
                    GPIO.output(17,True)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,0)

                elif (servidor == 0 or servidor == 1) and (GPIO.input(Sensor) == True) and (GPIO.input(BtnPin1) == False and GPIO.input(BtnPin2) == False): # Sensores acionado e a porta em movimento
                    #Emiti mensagem no Display
                    print('Porta em movimento')
                    disp.image(image3)
                    disp.display()
                    time.sleep(0.1)

        	    # Buzzer Ligado
                    GPIO.output(17,False)

        	    # Motor abrindo porta
                    GPIO.output(MOTORD,True)
                    GPIO.output(MOTORE,False)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,0)

                elif (servidor == 0 or servidor == 1) and (GPIO.input(Sensor) == True) and (GPIO.input(BtnPin2) == True) and (GPIO.input(BtnPin1) == False): # Sensores acionado e a porta aberta
                     #Emiti mensagem no Display
                    print('Sensor Acionado - Porta Aberta')
                    disp.image(image1)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor Desligado
                    GPIO.output(MOTORD,False)
                    GPIO.output(MOTORE,False)

        	    # Buzzer Ligado
                    GPIO.output(17,False)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,0)

        #Grupo 2:
                elif (servidor == 0) and (GPIO.input(Sensor) == False) and (GPIO.input(BtnPin2) == True) and (GPIO.input(BtnPin1) == False): # Sensores no acionado e a porta aberta
                     #Emiti mensagem no Display
                    print('Porta Abertaaa')
                    disp.image(image1)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor Desligado
                    GPIO.output(MOTORD,False)
                    GPIO.output(MOTORE,False)

        	    # Buzzer Desligado
                    GPIO.output(17,True)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,1)

                elif (servidor == 0) and (GPIO.input(Sensor) == False) and (GPIO.input(BtnPin2) == False) and (GPIO.input(BtnPin1) == True): # Sensores no acionado e a porta fechada
                     #Emiti mensagem no Display
                    print('Abrindo Porta')
                    disp.image(image1)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor abre porta
                    GPIO.output(MOTORD,True)
                    GPIO.output(MOTORE,False)

        	    # Buzzer Desligado
                    GPIO.output(17,True)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,0)

                elif (servidor == 0) and (GPIO.input(Sensor) == True) and (GPIO.input(BtnPin2) == False) and (GPIO.input(BtnPin1) == True): # Sensores acionado e a porta fechada
                     #Emiti mensagem no Display
                    print('Abrindo Porta')
                    disp.image(image1)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor abre porta
                    GPIO.output(MOTORD,True)
                    GPIO.output(MOTORE,False)

        	    # Buzzer Ligado
                    GPIO.output(17,False)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,0)
        #Grupo 3:
                elif (servidor == 1) and (GPIO.input(Sensor) == False) and (GPIO.input(BtnPin2) == True) and (GPIO.input(BtnPin1) == False): # Sensores nao acionado e a porta aberta
                     #Emiti mensagem no Display
                    print('Fechando Porta')
                    disp.image(image2)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor fecha porta
                    GPIO.output(MOTORD,False)
                    GPIO.output(MOTORE,True)

        	    # Buzzer Desligado
                    GPIO.output(17,True)

        	    #Destrava tranca, acionando o rel
                    GPIO.output(Rele,0)

                elif (servidor == 1) and (GPIO.input(Sensor) == True) and (GPIO.input(BtnPin2) == False) and (GPIO.input(BtnPin1) == True): # Sensores acionado e a porta fechada
                     #Emiti mensagem no Display
                    print('Porta Fechada')
                    disp.image(image2)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor Desligado
                    GPIO.output(MOTORD,False)
                    GPIO.output(MOTORE,False)

        	    # Buzzer Desligado
                    GPIO.output(17,False)

        	    #trava tranca, no acionando o rel
                    GPIO.output(Rele,1)

                elif (servidor == 1) and (GPIO.input(Sensor) == False) and (GPIO.input(BtnPin2) == False) and (GPIO.input(BtnPin1) == True): # Sensores no acionado e a porta fechada
                     #Emiti mensagem no Display
                    print('Acionado Sensor - Porta Fechada')
                    disp.image(image2)
                    disp.display()
                    time.sleep(0.1)

        	    # Motor Desligado
                    GPIO.output(MOTORD,False)
                    GPIO.output(MOTORE,False)

        	    # Buzzer ligado
                    GPIO.output(17,True)

        	    #trava tranca, no acionando o rel
                    GPIO.output(Rele,1)

        except KeyboardInterrupt:
            # Ctrl+C foi pressionado
        	pass

        # Limpa configura
        GPIO.cleanup()
