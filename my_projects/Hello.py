from manimlib.imports import *

class WriteSome(Scene):
    def construct(self):
        hello_penghui=TextMobject(
            "Hello,Penghui",
            color=YELLOW)
        
        welcome=TextMobject(
            "Welcome to Manim",
            color=BLUE
        )
        welcome.scale(2.5)

        self.play(Write(hello_penghui))
        self.wait(1)
        self.play(ApplyMethod(hello_penghui.scale, 2.5))
        self.play(Transform(hello_penghui,welcome))
        self.wait(2)

class Shoot(Scene):
    def construct(self):

        ## Making aim_scope
        circle_1=Circle(color=BLUE)
        circle_2=Circle(color=RED, fill_color=RED,fill_opacity=1)
        circle_2.scale(0.1)
        line_1=Line(np.array([-1,0,0]),np.array([1,0,0]))
        line_2=Line(np.array([0,1,0]),np.array([0,-1,0]))
        aim_scope=VGroup(circle_1, circle_2,line_1,line_2)

        ## Making target
        target_list=[]
        for i in range(3):
            for j in range(5):
                target_ij=Circle(color=WHITE,fill_color=YELLOW,fill_opacity=0.5)
                target_ij.scale(0.4)
                target_ij.shift(np.array([-4+j*2,-2+i*2,0]))
                self.play(FadeIn(target_ij,))
                target_list.append(target_ij)

        self.wait(1)

        ## Animation
        def shoot(i,j):
            target_ij=target_list[j+i*5]
            self.play(ApplyMethod(aim_scope.next_to,target_ij,0))
            self.play(ApplyMethod(target_ij.set_fill,GREY))
            self.wait(0.2)
            ij=TextMobject(str((i,j)), color = GREY)
            ij.next_to(target_ij,DOWN)
            self.play(Write(ij))
            self.wait(0.5)
            return 0
        
        self.add(aim_scope)
        shoot(0,4)
        shoot(2,2)
        shoot(1,3)
        self.wait(1)


# LOVE_DEATH_ROBOTS
class LDR(Scene):
    def construct(self):
        ## LOVE
        love_square=Square(color=RED,fill_color=RED,fill_opacity=0.5)
        love_square.rotate(PI/4)
        love_circle_1=Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        love_circle_2=Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        love_circle_1.move_to(love_square.get_center()+(LEFT+UP)*np.sqrt(2)/2)
        love_circle_2.move_to(love_square.get_center()+(RIGHT+UP)*np.sqrt(2)/2)
        love=VGroup(love_square,love_circle_1,love_circle_2)

        ## DEATH
        rect_1=Rectangle(height=0.7,width=4,color=RED, fill_color=RED, fill_opacity=0.5)
        rect_2=Rectangle(height=0.7,width=4,color=RED, fill_color=RED, fill_opacity=0.5)
        rect_1.rotate(PI/4)
        rect_2.rotate(-PI/4)
        death=VGroup(rect_1,rect_2)


        ##ROBOT
        square=Square(color=RED, fill_color=RED, fill_opacity=0.5)
        square.scale(1.6)
        eye1=Circle(color=RED, fill_color=BLACK, fill_opacity=0.5)
        eye2=Circle(color=RED, fill_color=BLACK, fill_opacity=0.5)
        eye1.scale(0.4)
        eye2.scale(0.4)
        eye1.move_to(square.get_center()+(0.6*UP+0.7*LEFT))
        eye2.move_to(square.get_center()+(0.6*UP+0.7*RIGHT))
        robot=VGroup(square,eye1,eye2)
        robot.shift(RIGHT*4)
        
        ##LINE & TEXT
        sep_line=Line(np.array([-4,-3,0]),np.array([4,-3,0]))
        title=TexMobject("LOVE \ \quad DEATH\  \& \  ROBOTS")
        title.scale(1.5)
        title.shift(DOWN*3)

        group_all=VGroup(love,death,robot,sep_line,title)
        
        ## Insert texts begin
        """ hello_penghui=TextMobject(
            "Hello,Penghui",
            color=YELLOW)
        
        welcome=TextMobject(
            "Welcome to Manim",
            color=BLUE
        )
        welcome.scale(2.5)

        self.play(Write(hello_penghui))
        self.wait(1)
        self.play(ApplyMethod(hello_penghui.scale, 2.5))
        self.play(Transform(hello_penghui,welcome))
        self.wait(2)
        self.play(FadeOut(hello_penghui))
        self.wait(2) """

        ## Insert texts end


        ## Animation
        self.play(ShowCreation(love))
        self.wait(0.5)
        self.play(ApplyMethod(love.shift,LEFT*4))
        self.wait(0.5)
        self.play(ShowCreation(death))
        self.wait(0.5)
        self.play(ShowCreation(robot))
        self.wait(0.5)
        self.play(ApplyMethod(love.set_opacity,1),
        ApplyMethod(death.set_opacity,1),
        ApplyMethod(robot.set_opacity,1)
        )
        self.wait(0.5)
        self.play(FadeIn(sep_line))
        self.wait(0.5)
        self.play(Transform(sep_line,title))
        self.wait(0.5)
        self.play(ApplyMethod(group_all.shift,UP*0.3))
        self.wait(1)

class LaTex(Scene):

    def construct(self):
        title= TexMobject("This  is some \\LaTex")
        basel= TexMobject(
            "\\sum_{n=1}^\\infty"
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title,basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel,UP)
        )
        self.wait(1)