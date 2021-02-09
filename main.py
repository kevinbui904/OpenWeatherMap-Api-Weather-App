import requests, json
from graphics import *

#function to quickly draw triangle from points a,b,and c
def Triangle(a,b,c,win):
    triangle = Polygon(a,b,c)
    triangle.setFill('black')
    triangle.draw(win)
    return#

#function to quickly draw rectangle from point1 and point2
def drawRectangle(Point1,Point2,win):
    rect = Rectangle(Point1,Point2)
    rect.setFill('black')
    rect.draw(win)
    return rect

#function to quickly draw rectangle from point center and pixeled
#radius value
def drawCircle(center,radius,win):
    circle = Circle(center,radius)
    circle.setFill('black')
    circle.setOutline('grey')
    circle.draw(win)
    return circle

#function to quickly draw octagons with 8 different points as parameter
def drawSnowFlake(Point1,Point2,Point3,Point4,Point5,Point6,Point7,Point8,win):
    aPolygon = Polygon(Point1,Point2,Point3,Point4,Point5,Point6,Point7,Point8)
    aPolygon.setFill('black')
    aPolygon.setOutline('grey')
    aPolygon.draw(win)
    return #nothing

#function to quickly write text to the screen,
#centered at Point1, font of 'size', style: 'italic','bold','underline'
#message in string. Return text object so it can be undrawn
def drawText(Point1,size,style,message,win):
    text = Text(Point1, message)
    text.setSize(size)
    text.setStyle(style)
    text.draw(win)
    return text

#function to draw cloud centered at (250,300), return
#cloud's center so other icon can be built
def cloud(win,scale,a=250,b=300):
    c = 40*scale
    drawCircle(Point(a,b), c, win)
    drawCircle(Point(a-50*scale,b-25*scale), c*0.85,win)
    drawCircle(Point(a+50*scale,b-25*scale),c*0.80,win)
    drawRectangle(Point(a-50*scale,b-25*scale),Point(a+50*scale,b-59*scale), win)
    return a,b

#function that draw a scalable sun
def sunny(win,scale):
#draw Circle
    core = Circle(Point(250,325), 45*scale)
    core.setFill('black')

#set center of triangle to be center of Circle
    centerX = core.getCenter().getX()
    centerY = core.getCenter().getY()
#make triangles
    Triangle(Point(centerX+115*0.50*scale,centerY+25*0.50*scale), Point(centerX+115*0.50*scale,centerY-25*0.50*scale),
            Point(centerX+125*0.50*scale,centerY),win)
    Triangle(Point(centerX-115*0.50*scale,centerY+25*0.50*scale), Point(centerX-115*0.50*scale,centerY-25*0.50*scale),
            Point(centerX-125*0.50*scale,centerY),win)
    Triangle(Point(centerX+25*0.50*scale,centerY+115*0.50*scale), Point(centerX-25*0.50*scale,centerY+115*0.50*scale),
            Point(centerX,centerY+125*0.50*scale),win)
    Triangle(Point(centerX+25*0.50*scale,centerY-115*0.50*scale), Point(centerX-25*0.50*scale,centerY-115*0.50*scale),
            Point(centerX,centerY-125*0.50*scale),win)
    Triangle(Point(centerX+80*0.50*scale,centerY+115*0.50*scale), Point(centerX+115*0.50*scale,centerY+80*0.50*scale),
            Point(centerX+110*0.50*scale,centerY+110*0.50*scale),win)
    Triangle(Point(centerX+80*0.50*scale,centerY-115*0.50*scale), Point(centerX+115*0.50*scale,centerY-80*0.50*scale),
            Point(centerX+110*0.50*scale,centerY-110*0.50*scale),win)
    Triangle(Point(centerX-80*0.50*scale,centerY-115*0.50*scale), Point(centerX-115*0.50*scale,centerY-80*0.50*scale),
            Point(centerX-110*0.50*scale,centerY-110*0.50*scale),win)
    Triangle(Point(centerX-80*0.50*scale,centerY+115*0.50*scale), Point(centerX-115*0.50*scale,centerY+80*0.50*scale),
            Point(centerX-110*0.50*scale,centerY+110*0.50*scale),win)
    core.draw(win)
    return #nothing

#draw thunderStorm icon based on cloud function
def thunderStorm(win,scale):
    center = cloud(win,scale*0.85,b=350)
    a = center[0]
    b = center[1]
    scale = scale*1.3
    bolt = Polygon(Point(a-10*scale,b-40*scale), Point(a-30*scale,b-60*scale),
            Point(a-10*scale,b-60*scale),Point(a+10*scale,b-40*scale))
    bolt2 = Polygon(Point(a-5*scale,b-50*scale),Point(a+20*scale,b-50*scale),
            Point(a-30*scale,b-90*scale))
    bolt2.setFill('black')
    bolt.setFill('black')
    bolt.draw(win)
    bolt2.draw(win)
    return# nothing

#draw snow icon
def snowy(win,scale):
    #original snowflake was too big, so scaled down
    scale = scale *0.65
    #establish center of snowflake as a point
    x,y = 250,325
    #draw snowflake
    drawSnowFlake(Point(x-10*scale,y+50*scale), Point(x-10*scale,y+65*scale),
                    Point(x-20*scale,y+80*scale),Point(x-10*scale,y+100*scale),
                        Point(x+10*scale,y+100*scale),Point(x+20*scale,y+80*scale),
                            Point(x+10*scale,y+65*scale),Point(x+10*scale,y+50*scale),win)

    drawSnowFlake(Point(x-10*scale,y-50*scale), Point(x-10*scale,y-65*scale),
                    Point(x-20*scale,y-80*scale),Point(x-10*scale,y-100*scale),
                        Point(x+10*scale,y-100*scale),Point(x+20*scale,y-80*scale),
                            Point(x+10*scale,y-65*scale),Point(x+10*scale,y-50*scale),win)

    drawSnowFlake(Point(x-50*scale,y-10*scale), Point(x-65*scale,y-10*scale),
                        Point(x-80*scale,y-20*scale),Point(x-100*scale,y-10*scale),
                            Point(x-100*scale,y+10*scale),Point(x-80*scale,y+20*scale),
                                Point(x-65*scale,y+10*scale),Point(x-50*scale,y+10*scale),win)

    drawSnowFlake(Point(x+50*scale,y-10*scale), Point(x+65*scale,y-10*scale),
                    Point(x+80*scale,y-20*scale),Point(x+100*scale,y-10*scale),
                        Point(x+100*scale,y+10*scale),Point(x+80*scale,y+20*scale),
                            Point(x+65*scale,y+10*scale),Point(x+50*scale,y+10*scale),win)

    drawSnowFlake(Point(x+35*scale,y+25*scale),Point(x+25*scale,y+35*scale),
                    Point(x+45*scale,y+55*scale),Point(x+50*scale,y+75*scale),
                        Point(x+75*scale,y+85*scale),Point(x+85*scale,y+75*scale),
                            Point(x+80*scale,y+53*scale), Point(x+55*scale,y+45*scale),win)

    drawSnowFlake(Point(x-35*scale,y+25*scale),Point(x-25*scale,y+35*scale),
                    Point(x-45*scale,y+55*scale),Point(x-50*scale,y+75*scale),
                        Point(x-75*scale,y+85*scale),Point(x-85*scale,y+75*scale),
                            Point(x-80*scale,y+53*scale), Point(x-55*scale,y+45*scale),win)

    drawSnowFlake(Point(x+35*scale,y-25*scale),Point(x+25*scale,y-35*scale),
                    Point(x+45*scale,y-55*scale),Point(x+50*scale,y-75*scale),
                        Point(x+75*scale,y-85*scale),Point(x+85*scale,y-75*scale),
                            Point(x+80*scale,y-53*scale), Point(x+55*scale,y-45*scale),win)

    drawSnowFlake(Point(x-35*scale,y-25*scale),Point(x-25*scale,y-35*scale),
                    Point(x-45*scale,y-55*scale),Point(x-50*scale,y-75*scale),
                        Point(x-75*scale,y-85*scale),Point(x-85*scale,y-75*scale),
                            Point(x-80*scale,y-53*scale), Point(x-55*scale,y-45*scale),win)
    #center of the snowflake, nested to get the extra line inside the octagon
    for i in [1,0.65,0.35]:
        scale = scale * i
        center = Polygon(Point(x-10*scale,y+50*scale),Point(x+10*scale,y+50*scale),
                            Point(x+25*scale,y+35*scale),Point(x+35*scale,y+25*scale),
                                Point(x+50*scale,y+10*scale),Point(x+50*scale,y-10*scale),
                                    Point(x+35*scale,y-25*scale),Point(x+25*scale,y-35*scale),
                                        Point(x+10*scale,y-50*scale),Point(x-10*scale,y-50*scale),
                                            Point(x-25*scale,y-35*scale),Point(x-35*scale,y-25*scale),
                                                Point(x-50*scale,y-10*scale),Point(x-50*scale,y+10*scale),
                                                    Point(x-35*scale,y+25*scale),Point(x-25*scale,y+35*scale))

        center.setOutline('grey')
        center.setFill('black')
        center.draw(win)
    return

#makes cloudy icon from cloud function
def cloudy(win,scale):
    cloud(win,0.95,b=350)
    cloud(win,0.85,a=265,b=335)
    return #nothing

#make rainy icon from cloud function
def rainy(win,scale):
    center = cloud(win,scale*0.85,b=350)
    a = center[0]
    b = center[1]
    #draw water droplets
    for i in range(3):
        for n in range(5):
            drawRectangle(Point(a-(50*scale)+(22*n*scale), b-(50*scale)-(25*i*scale)), Point(a-(45*scale)+(22*n*scale), b-(65*scale)-(25*i*scale)),win)
    return #nothing

#make tornado icon
def tornadoey(win,scale):
    #center of drawing
    x,y = 250,300
    drawRectangle(Point(x-50*scale,y), Point(x+50*scale,y+10*scale), win)
    drawRectangle(Point(x-80*scale,y+20*scale), Point(x+30*scale,y+30*scale), win)
    drawRectangle(Point(x-30*scale,y+40*scale), Point(x+50*scale,y+50*scale), win)
    drawRectangle(Point(x-50*scale,y+60*scale), Point(x+60*scale,y+70*scale), win)
    drawRectangle(Point(x-70*scale,y+80*scale), Point(x+30*scale,y+90*scale), win)
    drawRectangle(Point(x-20,y-10*scale), Point(x+70*scale,y-20*scale), win)
    drawRectangle(Point(x-40,y-30*scale), Point(x+30*scale,y-40*scale), win)
    drawRectangle(Point(x-30,y-50*scale), Point(x+10*scale,y-60*scale), win)
    return

#create icon for fog, haze, mist, dust, etc...
def impairedVisiony(win,scale):
    x,y = 250,300
    eye = Oval(Point(x-70*scale,y-40*scale), Point(x+70*scale,y+40*scale))
    eye.setOutline('grey')
    eye.setFill('grey')
    eye.draw(win)

    drawCircle(eye.getCenter(),30*scale,win)

    for i in range(3):
        drawRectangle(Point(x-(35*scale)+30*i*scale,y+35*scale),
                    Point(x-(25*scale)+30*i*scale,y+65*scale),win)

    cross = Polygon(eye.getP1(),Point(eye.getP1().getX()+30*scale,eye.getP1().getY()),
                    Point(eye.getP2().getX()+30*scale,eye.getP2().getY()), eye.getP2())
    cross2 = Polygon(Point(x-100*scale,y+40*scale), Point(x-70*scale,y+40*scale),
                        Point(x+70*scale,y-40*scale), Point(x+40*scale,y-40*scale))
    cross2.setFill('black')
    cross.setFill('black')
    cross.draw(win)
    cross2.draw(win)
    return #nothing

#make a class to store values from API call:
class Weather:
    def __init__(self,x):
        #name is stored in x dictionary with key 'name'
        self.name = x['name']
        #if the city name is more than 20 characters long,
        #abbreviate the city name, separated by a '.'
        if len(self.name)>20:
            abbr = []
            list = self.name.split(' ')
            for item in list:
                abbr.append(item[0])
            newName = '.'.join(abbr)
            self.name = newName

        #country is stored in a nested dictionary x['sys']['country']
        self.country = x['sys']['country']
        #point to x dictionary, 'weather'key, index 0 of 'weather' value, 'main' key
        self.condition = x['weather'][0]['main']
        #point to x dictionary, key 'main', then key 'temp/temp_min/temp_max'
        #convert that number value to Celcius (convert string to float then - 273)
        #then round to nearest 2 digits after decimal point
        self.temp = round((float(x['main']['temp']) - 273),2)
        self.minTemp = round((float(x['main']['temp_min']) - 273),2)
        self.maxTemp = round((float(x['main']['temp_max']) - 273),2)

    #method to return instance values
    def getName(self):
        return self.name

    def getCondition(self):
        return self.condition

    def getTemp(self):
        return self.temp, self.minTemp, self.maxTemp

    def getCountry(self):
        return self.country

#create user interface:
def userInterface(win):

    greeting = drawText(Point(250,400),20,'bold',
                ("Input city name below, \nuse [City, Country]\n for best result \n CLICK anywhere to proceed"),win)

    userInput = Entry(Point(250,300),15)
    userInput.setFill('grey')
    userInput.draw(win)

    #make map button
    mapInstruction = drawText(Point(250,200),20, 'bold',
                'Alternatively, press the button to\n mannually select longitude/latitude', win)

    button = Circle(Point(250,100),50)
    button.setFill('red')
    button.draw(win)

    textMap = drawText(button.getCenter(), 20, 'bold', 'MAP',win)

    #if the user click on the red button, return True so that
    #the map window pops up,ignoring whatever is in the input textbox
    if (200 < win.getMouse().getX() < 300) and (50 < win.getMouse().getY() < 250):
        button.undraw()
        textMap.undraw()
        mapInstruction.undraw()
        userInput.undraw()
        greeting.undraw()
        return True

    #if user does not click on red button, take whatever value is in
    #the input textbox and return it
    else:
        button.undraw()
        textMap.undraw()
        mapInstruction.undraw()
        userInput.undraw()
        greeting.undraw()
        return userInput.getText()

def main():
    #set the while loop so that user can quit whenever they want
    #or they can just be stuck in an unending cycle of Weathery App!
    play = True
    while play == True:
        #need this API key to ping openweathermap
        apiKey = "1b6a8055a73770e2b8b2fd5c344cb7fb"

        # base_url variable to store url
        baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

        #create the window of the program
        win = GraphWin("KB's Weathery App", 500,500)
        win.setCoords(0,0,500,500)

        #store userInput in cityName
        cityName = userInterface(win)

        #if user did not press on the red button
        #make standard API call with city name
        if cityName != True:

            completeUrl = baseUrl  + "q=" + cityName+ "&appid=" + apiKey

        #if user press red button
        #make API call using latitude/longitude
        #of the generated map (lines 284-287)
        else:

            win0 = GraphWin("KB's Weathery mApp", 896, 532)
            win0.setCoords(-180, -90, 180, 90)
            earth = Image(Point(0, 0), "worldmap.v1.gif")
            earth.draw(win0)

            xCoord = str(win0.getMouse().getX())
            yCoord = str(win0.getMouse().getY())

            completeUrl = baseUrl + 'lat=' + yCoord +'&lon='+ xCoord + '&cnt=1' +'&appid=' + apiKey
            #after the API is called, close the map window
            win0.close()

        # return the API response and store it
        response = requests.get(completeUrl)

        # json method of response object
        # convert json format data into
        # python format data, makes it readable
        x = response.json()

        #store all possible weather condition from API
        #into a dictionary that will return the corresponding
        #draw instructions
        weatherDictionary = {'Thunderstorm':thunderStorm,'Drizzle':rainy,'Rain':rainy,'Snow':snowy,
                            'Mist':impairedVisiony,'Smoke':impairedVisiony,'Haze':impairedVisiony,
                            'Dust':impairedVisiony,'Fog':impairedVisiony,'Sand':impairedVisiony,
                            'Dust':impairedVisiony,'Ash':impairedVisiony,'Squall':impairedVisiony,
                            'Tornado':tornadoey,'Clear':sunny,'Clouds':cloudy}


        # x points to nested dictionary. Key 'cod' refers to the
        #API's response if input city is valid, if 'cod' is equal to
        #200, and id != 0, it means that the API is being pointed
        #to a city that exist
        if x['cod'] == 200 and x['id']!=0 :

            #create object containing all information that API gives back
            cityWeather = Weather(x)
            #draw the picture from dictionary to screen
            draw = weatherDictionary[cityWeather.getCondition()]
            draw(win,1)

            #draw instruction text to screen
            drawText(Point(250,450),30,'bold', cityWeather.getName() +', ' +
                        cityWeather.getCountry(), win)

            drawText(Point(175,175),15,'bold','Current Temp:',win)
            drawText(Point(175,150),15,'bold','      Min Temp:',win)
            drawText(Point(175,125),15,'bold','     Max Temp:',win)
            drawText(Point(175,100),15,'bold','      Condition:',win)

            drawText(Point(325,175),15,'italic',(str(cityWeather.getTemp()[0])+ ' Celsius'),win)
            drawText(Point(325,150),15,'italic',(str(cityWeather.getTemp()[1])+ ' Celsius'),win)
            drawText(Point(325,125),15,'italic',(str(cityWeather.getTemp()[2])+ ' Celsius'),win)
            drawText(Point(325,100),15,'italic',cityWeather.getCondition(),win)

            #draw quit button

            button = Circle(Point(0,0),100)
            button.setFill('grey')
            button.draw(win)

            drawText(Point(30,30),15,'bold', 'Quit', win)

            if (win.getMouse().getX() < 100) and (win.getMouse().getY() < 100):
                play = False
                win.close()
            else:
                play = True
                win.close()
        #if cod == 200 but id ==0, it means that the API have weather
        #data for the specified coordinates but that coordinate is
        #not a city (hence id = 0)
        elif x['cod'] == 200 and x['id'] == 0:
            drawText(Point(250,250),30,'bold italic', "That's not a valid city\n...YET!",win)
            drawText(Point(250,100),25,'italic','press to try again',win)
            win.getMouse()
            win.close()

        #if cod == 400, it means that user is trying to make an empty
        #API call (as in they didn't specify any parameters)
        elif x['cod'] == '400':
            drawText(Point(250,250),30,'bold italic', "Enter something PLEASE",win)
            drawText(Point(250,100),25,'italic','press to try again',win)
            win.getMouse()
            win.close()

        #the API don't have data of this region
        else:
            drawText(Point(250,250),30,'bold italic', "API have no data",win)
            drawText(Point(250,100),25,'italic','press to try again',win)
            win.getMouse()
            win.close()


if __name__ == "__main__":
    main()

#create dictionary for different weather condition
