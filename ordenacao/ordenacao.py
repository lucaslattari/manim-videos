from manimlib import *
import numpy as np

class Cena1(Scene):
    def construct(self):
        books = Group(
            ImageMobject("book1.png"),
            ImageMobject("book2.png").scale(0.8),
            ImageMobject("book3.png").scale(0.9),
            ImageMobject("book4.png").scale(0.8),
        ).set_x(-2)

        prat = ImageMobject("prat.png").scale(0.17)
        prat.set_x(0).set_y(-1.94)
        self.add(prat)

        for i, b in enumerate(books):
            if i > 0:
                b.next_to(books[i - 1], RIGHT*0.4)

        books[0].set_y(0.4)
        books[1].set_y(0)
        books[2].set_y(0.2)
        books[3].set_y(0.03).shift(RIGHT*0.49)

        dot=Dot(point=np.array([8,-1,0]))
        self.play(GrowFromPoint(mobject=books[0],point=dot),run_time=1.5)
        self.play(GrowFromPoint(mobject=books[1],point=dot),run_time=1.5)
        self.play(GrowFromPoint(mobject=books[2],point=dot),run_time=1.5)
        self.play(GrowFromPoint(mobject=books[3],point=dot),run_time=1.5)
        self.play(Rotate(books[3], PI / 8))
        self.wait(3.5)

        t_livro1 = Text("D", color=WHITE).set_stroke(BLACK, 10, background=True)
        t_livro1.set_x(books[0].get_x())
        t_livro1.set_y(books[0].get_y() - 0.1)
        t_livro1.scale(1.2)

        t_livro2 = Text("C", color=WHITE).set_stroke(BLACK, 10, background=True)
        t_livro2.set_x(books[1].get_x() + 0.04)
        t_livro2.set_y(books[1].get_y() - 0.35)
        t_livro2.scale(1.2)

        t_livro3 = Text("B", color=WHITE).set_stroke(BLACK, 10, background=True)
        t_livro3.set_x(books[2].get_x() - 0.03)
        t_livro3.set_y(books[2].get_y())
        t_livro3.scale(1.2)

        t_livro4 = Text("A", color=WHITE).set_stroke(BLACK, 10, background=True)
        t_livro4.set_x(books[3].get_x() + 0.07)
        t_livro4.set_y(books[3].get_y() - 0.1)
        t_livro4.rotate(0.4).scale(1.2)

        self.play(Write(t_livro1), Write(t_livro2), Write(t_livro3), Write(t_livro4))
        self.wait()

        self.play(prat.animate.scale(2))
        self.play(FadeOut(prat))

        self.play(
            books[0].animate.shift(DOWN*1.5), t_livro1.animate.shift(DOWN*1.5),
            books[1].animate.shift(DOWN*1.5), t_livro2.animate.shift(DOWN*1.5),
            books[2].animate.shift(DOWN*1.5), t_livro3.animate.shift(DOWN*1.5),
            books[3].animate.shift(DOWN*1.5), t_livro4.animate.shift(DOWN*1.5),
        )
        self.wait(1.5)

        eye = SVGMobject("eye.svg").scale(0.5)
        arrow = SVGMobject("arrow.svg").scale(0.5)

        arrow.next_to(books[0], UP)
        eye.next_to(arrow, UP)
        eye[0].set_style(fill_opacity=1,stroke_width=2,fill_color=WHITE).set_stroke(color=BLACK)
        arrow[0].set_style(fill_opacity=1,stroke_width=2,fill_color=WHITE).set_stroke(color=BLACK)

        print(len(arrow), len(eye))
        self.play(ShowCreation(arrow), ShowCreation(eye))
        self.wait(0.5)

        self.play(arrow.animate.shift(RIGHT*1.1), eye.animate.shift(RIGHT*1.1))
        self.wait(0.5)

        self.play(arrow.animate.shift(RIGHT*0.9), eye.animate.shift(RIGHT*0.9))
        self.wait(0.5)

        self.play(arrow.animate.shift(RIGHT*1), eye.animate.shift(RIGHT*1))
        self.wait(0.5)

        self.play(
            ClockwiseTransform(books[3], books[0]),
            t_livro4.animate.move_to(t_livro1).rotate(-0.4).shift(RIGHT*0.1),
            ClockwiseTransform(books[0], books[3]),
            t_livro1.animate.move_to(t_livro4).rotate(0.4).shift(LEFT*0.1),
        )

        self.wait(2)

        self.play(arrow.animate.shift(LEFT*1.9), eye.animate.shift(LEFT*1.9))
        self.wait(1)

        self.play(arrow.animate.shift(RIGHT*0.9), eye.animate.shift(RIGHT*0.9))
        self.wait(1)

        self.play(
            ClockwiseTransform(books[1], books[2]),
            t_livro3.animate.move_to(t_livro2).shift(UP*0.5).shift(LEFT*0.05),
            ClockwiseTransform(books[2], books[1]),
            t_livro2.animate.move_to(t_livro3).shift(DOWN*0.5).shift(RIGHT*0.05),
        )
        self.wait(2)

        self.play(
            Uncreate(arrow), Uncreate(eye),
            FadeOutToPoint(books[0], [0, -4, 0]), FadeOutToPoint(t_livro1, [0, -4, 0]),
            FadeOutToPoint(books[1], [0, -4, 0]), FadeOutToPoint(t_livro2, [0, -4, 0]),
            FadeOutToPoint(books[2], [0, -4, 0]), FadeOutToPoint(t_livro3, [0, -4, 0]),
            FadeOutToPoint(books[3], [0, -4, 0]), FadeOutToPoint(t_livro4, [0, -4, 0]),
        )
        self.wait()

class Cena2(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Ordenação por", stroke_width=3, stroke_color=BLACK).scale(1.75)
        ord2 = Text("Seleção", stroke_width=3, stroke_color=BLACK).scale(1.75)
        g = VGroup(ord, ord2).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class Extra1(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Comparar e trocar itens", stroke_width=3, stroke_color=BLACK)
        ord2 = Text("de posição são operações", stroke_width=3, stroke_color=BLACK)
        ord3 = Text("do algoritmo.", stroke_width=3, stroke_color=BLACK)

        g = VGroup(ord, ord2, ord3).arrange(DOWN)
        ord[:8].set_color(RED).set_stroke(BLACK, width=3)
        ord[11:17].set_color(RED).set_stroke(BLACK, width=3)
        ord2[3:10].set_color(RED).set_stroke(BLACK, width=3)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class Cena3(Scene):
    def construct(self):
        eq_compl = Tex("n \\times (n-1) = n^2 - n", isolate=["n^2 - n"])

        self.play(Write(eq_compl[0]))
        self.play(eq_compl[0].animate.scale(2.5))
        self.wait(5.5)
        self.play(eq_compl[0].animate.shift(LEFT))
        self.wait()
        eq_compl[1].scale(2.5).next_to(eq_compl[0], RIGHT).shift(0.2*UR)
        self.play(Write(eq_compl[1]))
        self.play(eq_compl[1].animate.set_color(BLUE))
        self.wait()
        self.play(eq_compl.animate.shift(UP*2.7))
        self.wait()

        axes = Axes((0, 10), (0, 20))
        axes.scale(0.85).to_edge(DOWN)
        self.play(ShowCreation(axes, lag_ratio=0.01, run_time=1))

        x_labels = [
            Tex("0"), Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7"),
            Tex("8"), Tex("9"), Tex("10")
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(axes.c2p(i, 0.2), DOWN).scale(0.5)
            self.add(x_labels[i])

        y_labels = [
            Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7"),
            Tex("8"), Tex("9"), Tex("10"), Tex("11"), Tex("12"), Tex("13"),
            Tex("14"), Tex("15"), Tex("16"), Tex("17"),
            Tex("18")
        ]

        for i in range(len(y_labels)):
            y_labels[i].next_to(axes.c2p(0, i+1), LEFT).scale(0.5)
            if i >= 9:
                y_labels[i].shift(RIGHT*0.1)
            self.add(y_labels[i])

        graph = axes.get_graph(
            lambda x: x**2 - x,
            color=BLUE,
            x_range=[1, 4.5]
        )
        graph_label = Tex("f(n) = n^2 - n", color=BLUE, isolate=["n", "n^2"])
        graph_label.next_to(graph, UR)
        self.play(
            ShowCreation(graph),
            FadeInFromPoint(graph_label, [-1, -1, 0]),
        )
        self.wait(3)

        self.play(
            Uncreate(eq_compl), Uncreate(axes),
            Uncreate(x_labels[0]), Uncreate(x_labels[1]),
            Uncreate(x_labels[2]), Uncreate(x_labels[3]),
            Uncreate(x_labels[4]), Uncreate(x_labels[5]),
            Uncreate(x_labels[6]), Uncreate(x_labels[7]),
            Uncreate(x_labels[8]), Uncreate(x_labels[9]),
            Uncreate(x_labels[10]),
            Uncreate(y_labels[0]), Uncreate(y_labels[1]),
            Uncreate(y_labels[2]), Uncreate(y_labels[3]),
            Uncreate(y_labels[4]), Uncreate(y_labels[5]),
            Uncreate(y_labels[6]), Uncreate(y_labels[7]),
            Uncreate(y_labels[8]), Uncreate(y_labels[9]),
            Uncreate(y_labels[10]), Uncreate(y_labels[11]),
            Uncreate(y_labels[12]), Uncreate(y_labels[13]),
            Uncreate(y_labels[14]), Uncreate(y_labels[15]),
            Uncreate(y_labels[16]), Uncreate(y_labels[17]),
            Uncreate(graph)
        )

        self.play(graph_label.animate.shift(UP*1.8).shift(1.42*LEFT).scale(2.4), run_time=2)
        self.play(
            graph_label[1].animate.set_color(RED),
            graph_label[3].animate.set_color(RED),
            graph_label[4][0].animate.set_color(RED),
            graph_label[5].animate.set_color(RED),
        )

        eq_10_a_6=graph_label.copy()
        eq_10_a_6.set_x(graph_label.get_x()).set_y(graph_label.get_y())
        self.add(eq_10_a_6)
        self.play(
            eq_10_a_6.animate.shift(DOWN*2),
        )

        transf1 = Tex("10^6", color=RED).scale(1.3).set_x(eq_10_a_6[1].get_x()).set_y(eq_10_a_6[1].get_y()).shift(0.1*UP).shift(RIGHT*0.05)
        transf2 = Tex("(10^6)^2", color=RED).scale(1.3).set_x(eq_10_a_6[3].get_x()).set_y(eq_10_a_6[3].get_y()).shift(0.1*UP).shift(RIGHT*0.29)
        transf3 = Tex("10^6", color=RED).scale(1.3).set_x(eq_10_a_6[5].get_x()).set_y(eq_10_a_6[5].get_y()).shift(0.1*UP).shift(RIGHT*0.05)

        self.play(
            ReplacementTransform(eq_10_a_6[1], transf1),
            ReplacementTransform(eq_10_a_6[3], transf2),
            Uncreate(eq_10_a_6[4][0]),
            ReplacementTransform(eq_10_a_6[5], transf3),
        )
        self.wait(1.5)

        self.play(
            graph_label.animate.to_edge(2.8*LEFT),
            eq_10_a_6.animate.shift(2.8*LEFT),
            transf1.animate.shift(2.8*LEFT),
            transf2.animate.shift(2.8*LEFT),
            transf3.animate.shift(2.8*LEFT),
        )
        self.wait()

        trilhao = Tex("\\approx 10^{12} passos.", isolate=["passos."], color=BLUE).scale(2)
        trilhao.next_to(eq_10_a_6, RIGHT).shift(0.2*UP)
        trilhao[1].shift(RIGHT*0.3)
        self.play(Write(trilhao))
        self.wait(9.5)

        tempo_texto_1 = Text(
            "Assim, se um computador demorar meio segundo",
            font="Arial", font_size=25,
            t2c={"meio segundo": RED}
        )

        tempo_texto_2 = Text(
            "em cada operação, vai demorar 500 bilhões de segundos",
            font="Arial", font_size=25,
            t2c={"500 bilhões de segundos": WHITE}
        )

        tempo_texto_3 = Text(
            "para terminar, algo equivalente a 15 mil anos.",
            font="Arial", font_size=25,
            t2c={"15 mil anos": WHITE}
        )

        VGroup(tempo_texto_1, tempo_texto_2, tempo_texto_3).arrange(DOWN, buff=0.2)

        tempo_texto_1.shift(DOWN*2)
        tempo_texto_2.shift(DOWN*2)
        tempo_texto_3.shift(DOWN*2)

        self.play(Write(tempo_texto_1))
        self.play(Write(tempo_texto_2))
        self.play(Write(tempo_texto_3))
        self.wait(12)
        self.play(tempo_texto_2.animate.set_color_by_t2c({"500 bilhões de segundos": RED}))
        self.wait(4)
        self.play(tempo_texto_3.animate.set_color_by_t2c({"15 mil anos": RED}))
        self.wait()

        self.play(
            Uncreate(graph_label), Uncreate(eq_10_a_6),
            Uncreate(transf1), Uncreate(transf2), Uncreate(transf3),
            Uncreate(trilhao), Uncreate(tempo_texto_1),
            Uncreate(tempo_texto_2), Uncreate(tempo_texto_3)
        )
        self.wait(3)

class CenaQ(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Quicksort", stroke_width=3, stroke_color=BLACK).scale(1.75)

        self.play(Write(ord))
        self.play(Uncreate(ord))

class Cena4(Scene):
    def construct(self):
        array = VGroup(
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
        ).arrange(RIGHT, buff=0.1)

        numbers = VGroup(
            Tex("9"), Tex("2"), Tex("7"), Tex("3"),
            Tex("5"), Tex("4"), Tex("6"), Tex("8")
        )

        self.wait(2)
        titulo = Text("Quicksort").to_edge(UP)
        self.play(Write(titulo))
        self.wait(3)

        for a in array:
            self.play(Write(a), run_time=0.5)

        for a, n in zip(array, numbers):
            n.set_x(a.get_x())
            n.set_y(a.get_y())
            self.play(Write(n))

        self.wait()

        pivot_background = BackgroundRectangle(
            numbers[4], color=YELLOW, fill_opacity=0.3, buff=0.1
        )
        self.wait(1)
        self.play(ShowCreation(pivot_background))
        self.wait(1)

        pivot_label = Text("Pivô:", font="Times New Roman", font_size=25).next_to(titulo, DOWN).shift(LEFT*0.5)
        self.play(Write(pivot_label))
        self.wait(3)

        pivot_number_copy = numbers[4].copy()
        self.play(pivot_number_copy.animate.next_to(pivot_label, RIGHT*0.7).shift(DOWN*0.01).set_color(YELLOW))
        self.wait(2)

        self.play(
            numbers[0].animate.shift(DOWN*1), numbers[1].animate.shift(DOWN*1),
            numbers[2].animate.shift(DOWN*1), numbers[3].animate.shift(DOWN*1),
            numbers[4].animate.shift(DOWN*1), numbers[5].animate.shift(DOWN*1),
            numbers[6].animate.shift(DOWN*1), numbers[7].animate.shift(DOWN*1),
            Uncreate(pivot_background), FadeOut(numbers[4])
        )
        self.wait(3)

        arrow = SVGMobject("arrow.svg").scale(0.5).rotate(PI)

        arrow.next_to(numbers[0], DOWN)
        arrow[0].set_style(fill_opacity=1,stroke_width=2,fill_color=WHITE).set_stroke(color=BLACK)
        self.play(FadeIn(arrow))
        self.wait(5.5)

        #9
        self.play(numbers[0].animate.move_to(array[-1].get_start()).shift(DL*0.5))
        self.wait(4)

        #2
        self.play(arrow.animate.next_to(numbers[1], DOWN))
        self.wait(4.5)

        self.play(numbers[1].animate.move_to(array[0].get_start()).shift(DL*0.5))
        self.wait(7.3)

        #7
        self.play(arrow.animate.next_to(numbers[2], DOWN))
        self.wait(3.5)

        self.play(numbers[2].animate.move_to(array[-2].get_start()).shift(DL*0.5))
        self.wait(1)

        #3
        self.play(arrow.animate.next_to(numbers[3], DOWN))
        self.wait(3)

        self.play(numbers[3].animate.move_to(array[1].get_start()).shift(DL*0.5))
        self.wait(1)

        #4
        self.play(arrow.animate.next_to(numbers[5], DOWN))
        self.wait(0.25)

        self.play(numbers[5].animate.move_to(array[2].get_start()).shift(DL*0.5))
        self.wait(0.2)

        #6
        self.play(arrow.animate.next_to(numbers[6], DOWN))
        self.wait(0.25)

        self.play(numbers[6].animate.move_to(array[-3].get_start()).shift(DL*0.5))
        self.wait(0.75)

        #8
        self.play(arrow.animate.next_to(numbers[7], DOWN))
        self.wait(0.25)

        self.play(numbers[7].animate.move_to(array[-4].get_start()).shift(DL*0.5))
        self.wait(1.2)

        #pivo
        self.play(pivot_number_copy.animate.set_color(WHITE).move_to(array[3].get_start()).shift(DL*0.5))
        self.wait(0.2)

        self.play(FadeOut(arrow))
        self.wait(5.85)

        self.play(
            array[0].animate.set_color(YELLOW), array[1].animate.set_color(YELLOW),
            array[2].animate.set_color(YELLOW)
        )
        self.wait(5)

        self.play(
            array[0].animate.set_color(WHITE), array[1].animate.set_color(WHITE),
            array[2].animate.set_color(WHITE),

            array[4].animate.set_color(YELLOW), array[5].animate.set_color(YELLOW),
            array[6].animate.set_color(YELLOW), array[7].animate.set_color(YELLOW)
        )
        self.wait(7)

        self.play(
            array[4].animate.set_color(WHITE), array[5].animate.set_color(WHITE),
            array[6].animate.set_color(WHITE), array[7].animate.set_color(WHITE)
        )
        self.wait(1.5)

        #novo pivô, nova metade
        self.play(
            numbers[6].animate.next_to(pivot_label, RIGHT).set_color(YELLOW),
            numbers[7].animate.shift(DOWN), numbers[2].animate.shift(DOWN),
            numbers[0].animate.shift(DOWN)
        )
        self.wait(6)

        self.wait(3)
        self.play(
            numbers[7].animate.move_to(array[-1].get_start()).shift(DL*0.5)
        )
        self.play(
            numbers[2].animate.move_to(array[-2].get_start()).shift(DL*0.5),
        )
        self.play(
            numbers[0].animate.move_to(array[-3].get_start()).shift(DL*0.5),
        )
        self.wait(4)
        self.play(
            numbers[6].animate.set_color(WHITE).move_to(array[4].get_start()).shift(DL*0.5),
        )
        self.wait(1)

        self.play(
            array[-1].animate.set_color(YELLOW), array[-2].animate.set_color(YELLOW),
            array[-3].animate.set_color(YELLOW)
        )
        self.wait(2)

        self.play(
            array[-1].animate.set_color(WHITE), array[-2].animate.set_color(WHITE),
            array[-3].animate.set_color(WHITE)
        )

        #pivô 7
        self.wait(1)
        self.play(
            numbers[2].animate.next_to(pivot_label, RIGHT).set_color(YELLOW),
            numbers[0].animate.shift(DOWN),
            numbers[-1].animate.shift(DOWN)
        )

        self.wait(2)
        self.play(
            numbers[0].animate.move_to(array[-1].get_start()).shift(DL*0.5),
            numbers[-1].animate.move_to(array[-2].get_start()).shift(DL*0.5),
        )

        self.play(
            numbers[2].animate.set_color(WHITE).move_to(array[-3].get_start()).shift(DL*0.5),
            array[-1].animate.set_color(WHITE), array[-2].animate.set_color(WHITE),
            array[-3].animate.set_color(WHITE),
            Uncreate(pivot_label), Uncreate(titulo)
        )
        self.wait(2)

        self.play(
            Uncreate(array), Uncreate(numbers), Uncreate(pivot_number_copy)
        )
        self.wait(6)

class Cena5_2(Scene):
    def construct(self):
        eq_log = Tex("n \\times log(n)").scale(2)
        self.play(Write(eq_log))
        obs = Text("OBS: Os logs apresentados aqui são de base 2.").scale(0.5).to_edge(DOWN).shift(0.2*DOWN)
        self.play(Write(obs))
        self.wait(39)

        self.play(eq_log.animate.scale(1.5).to_edge(UP).set_color(WHITE), Uncreate(obs))
        self.wait(0.5)

        axes = Axes((0, 10), (0, 20))
        axes.scale(0.85).to_edge(DOWN)
        self.play(ShowCreation(axes, lag_ratio=0.01, run_time=1))

        x_labels = [
            Tex("0"), Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7"),
            Tex("8"), Tex("9"), Tex("10")
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(axes.c2p(i, 0.2), DOWN).scale(0.5)
            self.add(x_labels[i])

        y_labels = [
            Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7"),
            Tex("8"), Tex("9"), Tex("10"), Tex("11"), Tex("12"), Tex("13"),
            Tex("14"), Tex("15"), Tex("16"), Tex("17"),
            Tex("18")
        ]

        for i in range(len(y_labels)):
            y_labels[i].next_to(axes.c2p(0, i+1), LEFT).scale(0.5)
            if i >= 9:
                y_labels[i].shift(RIGHT*0.1)
            self.add(y_labels[i])

        import math
        graph = axes.get_graph(
            lambda x: x**2 - x,
            color=BLUE,
            x_range=[1, 4.5]
        )
        graph_label = Tex("f(n) = n^2 - n", color=BLUE, isolate=["f(","n", ") = ", "^2", "- 1"])
        graph_label.next_to(graph, UR).shift(1.3*LEFT)

        graph_log = axes.get_graph(
            lambda x: x * math.log(x, 2) - 1,
            color=RED,
            x_range=[1.7, 7]
        )
        graph_log_label = Tex("f(n) = n \\times log(n)", color=RED, isolate=["n"])
        graph_log_label.next_to(graph_log, 0.5*UR).shift(0.2*LEFT)
        self.play(
            ShowCreation(graph_log),
            FadeInFromPoint(graph_log_label, [-1, -1, 0]),
        )

        self.play(
            Uncreate(eq_log),
            ShowCreation(graph),
            FadeInFromPoint(graph_label, [-1, -1, 0]),
        )

        self.camera.frame.save_state()
        #self.play(self.camera.frame.move_to, graph_log)
        self.play(self.camera.frame.animate.shift(0.2*RIGHT).shift(DOWN))

        label_axis_x = Text("Total de livros", color=YELLOW).scale(0.4)
        label_axis_x.next_to(x_labels[-1], 3*UP).shift(0.3*LEFT)
        self.play(Write(label_axis_x))

        self.wait()

        label_axis_y = Text("Total de passos", color=YELLOW).scale(0.4)
        label_axis_y.next_to(y_labels[-1], 2.5*RIGHT).shift(0.6*UP)
        self.play(Write(label_axis_y))

        self.wait(5.75)

        self.play(
            Uncreate(label_axis_y),
            Uncreate(axes), Uncreate(label_axis_x),
            Uncreate(x_labels[0]), Uncreate(x_labels[1]),
            Uncreate(x_labels[2]), Uncreate(x_labels[3]),
            Uncreate(x_labels[4]), Uncreate(x_labels[5]),
            Uncreate(x_labels[6]), Uncreate(x_labels[7]),
            Uncreate(x_labels[8]), Uncreate(x_labels[9]),
            Uncreate(x_labels[10]),
            Uncreate(y_labels[0]), Uncreate(y_labels[1]),
            Uncreate(y_labels[2]), Uncreate(y_labels[3]),
            Uncreate(y_labels[4]), Uncreate(y_labels[5]),
            Uncreate(y_labels[6]), Uncreate(y_labels[7]),
            Uncreate(y_labels[8]), Uncreate(y_labels[9]),
            Uncreate(y_labels[10]), Uncreate(y_labels[11]),
            Uncreate(y_labels[12]), Uncreate(y_labels[13]),
            Uncreate(y_labels[14]), Uncreate(y_labels[15]),
            Uncreate(y_labels[16]), Uncreate(y_labels[17]),
            Uncreate(graph), Uncreate(graph_log), Uncreate(graph_label),
            FadeOut(graph_log_label)
        )

        self.wait(7.5)
        self.play(Restore(self.camera.frame))

        t1 = Text("Como a função do Quicksort (        ) cresce").scale(0.5)
        t2 = Text("mais lentamente, ela realiza menos operações para").scale(0.5)
        t3 = Text("mais livros, se comparada a Ordenação por Seleção (     ).").scale(0.5)
        t4 = Text("Assim, com mais livros, é melhor usar o Quicksort!").scale(0.5)

        t1[16:26].set_color(BLUE)
        t3[27:49].set_color(RED)
        t4[39:49].set_color(BLUE)

        texto = VGroup(t1, t2, t3, t4).arrange(DOWN, center=True, buff=0.2).shift(0.5*UP)
        t4.shift(DOWN*0.5)

        e1 = Tex("n \\times log(n)").set_color(BLUE)
        e2 = Tex("n^2 - n").set_color(RED)

        e1.next_to(t1[27], 0.4*RIGHT)
        e2.next_to(t3[50], 0.4*RIGHT)

        self.play(Write(texto), Write(e1), Write(e2), run_time=4)
        self.wait(6.2)

        self.play(Uncreate(texto), Uncreate(e1), Uncreate(e2))
        self.wait(3)

        graph_log_label.set_color(WHITE).set_x(0).set_y(0)
        graph_log_label.to_edge(UP).scale(2)
        self.play(FadeIn(graph_log_label))
        self.play(
            graph_log_label[1].animate.set_color(RED),
            graph_log_label[3].animate.set_color(RED),
            graph_log_label[5].animate.set_color(RED)
        )

        eq_10_a_6=graph_log_label.copy()
        eq_10_a_6.set_x(graph_log_label.get_x()).set_y(graph_log_label.get_y())
        self.add(eq_10_a_6)
        self.play(
            eq_10_a_6.animate.shift(DOWN*2),
        )

        transf1 = Tex("10^6", color=RED).scale(1.1).set_x(eq_10_a_6[1].get_x()).set_y(eq_10_a_6[1].get_y()).shift(0.1*UP).shift(RIGHT*0.05)
        transf2 = Tex("10^6", color=RED).scale(1.3).set_x(eq_10_a_6[3].get_x()).set_y(eq_10_a_6[3].get_y()).shift(0.1*UP).shift(RIGHT*0.05)
        transf3 = Tex("10^6", color=RED).scale(1.2).set_x(eq_10_a_6[5].get_x()).set_y(eq_10_a_6[5].get_y()).shift(0.1*UP)

        self.play(
            ReplacementTransform(eq_10_a_6[1], transf1),
            ReplacementTransform(eq_10_a_6[3], transf2),
            ReplacementTransform(eq_10_a_6[5], transf3)
        )

        self.wait()
        self.play(
            graph_label.animate.to_edge(2.8*LEFT),
            eq_10_a_6.animate.shift(2.8*LEFT),
            transf1.animate.shift(2.8*LEFT),
            transf2.animate.shift(2.8*LEFT),
            transf3.animate.shift(2.8*LEFT),
        )
        self.wait()

        seis_milhoes = Tex("\\approx 19 \\times 10^6 passos.", isolate=["passos."], color=WHITE).scale(1.5)
        seis_milhoes.next_to(eq_10_a_6, RIGHT)
        seis_milhoes[1].shift(RIGHT*0.2)
        self.play(Write(seis_milhoes))
        self.wait()

        tempo_texto_1 = Text(
            "Dessa vez, se um computador levar meio segundo para",
            font="Arial", font_size=25,
            t2c={"meio segundo": RED}
        )

        tempo_texto_2 = Text(
            "cada operação, isso vai demorar 19 milhões de segundos",
            font="Arial", font_size=25,
            t2c={"19 milhões de segundos": RED}
        )

        tempo_texto_3 = Text(
            "para terminar, pouco mais de 7 meses.",
            font="Arial", font_size=25,
            t2c={"7 meses": RED}
        )

        a = VGroup(tempo_texto_1, tempo_texto_2, tempo_texto_3).arrange(DOWN, buff=0.2)

        tempo_texto_1.shift(DOWN*2)
        tempo_texto_2.shift(DOWN*2)
        tempo_texto_3.shift(DOWN*2)

        self.play(Write(a))
        self.wait(4)

        self.play(
            Uncreate(graph_log_label), Uncreate(eq_10_a_6),
            Uncreate(transf1), Uncreate(transf2), Uncreate(transf3),
            Uncreate(seis_milhoes), Uncreate(tempo_texto_1),
            Uncreate(tempo_texto_2), Uncreate(tempo_texto_3)
        )
        self.wait()

class CenaC(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("CountingSort", stroke_width=3, stroke_color=BLACK).scale(1.75)

        self.play(Write(ord))
        self.wait(10)
        self.play(Uncreate(ord))

class Cena6(Scene):
    def construct(self):
        array = VGroup(
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1)
        ).arrange(RIGHT, buff=0.1)

        numbers = VGroup(
            Tex("1"), Tex("4"), Tex("1"), Tex("2"),
            Tex("7"), Tex("5"), Tex("2")
        )

        titulo = Text("Counting Sort").to_edge(UP)
        self.play(Write(titulo), Write(array))

        for a, n in zip(array, numbers):
            n.set_x(a.get_x())
            n.set_y(a.get_y())
            self.add(n)

        vector_label = Tex("Vetor:").scale(0.8)
        vector_label.next_to(array[0], LEFT)
        self.play(Write(vector_label))

        self.play(
            array[0].animate.shift(UP*0.5), array[1].animate.shift(UP*0.5),
            array[2].animate.shift(UP*0.5), array[3].animate.shift(UP*0.5),
            array[4].animate.shift(UP*0.5), array[5].animate.shift(UP*0.5),
            array[6].animate.shift(UP*0.5),
            numbers[0].animate.shift(UP*0.5), numbers[1].animate.shift(UP*0.5),
            numbers[2].animate.shift(UP*0.5), numbers[3].animate.shift(UP*0.5),
            numbers[4].animate.shift(UP*0.5), numbers[5].animate.shift(UP*0.5),
            numbers[6].animate.shift(UP*0.5),
            vector_label.animate.shift(UP*0.5)
        )
        self.wait(5)

        array_count = VGroup(
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1),
        ).arrange(RIGHT, buff=0.1)

        indices = VGroup(
            Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7")
        )

        numbers_count = VGroup(
            Tex("0"), Tex("0"), Tex("0"),
            Tex("0"), Tex("0"), Tex("0"), Tex("0")
        )

        for i, a in enumerate(array_count):
            if i < len(array):
                a.next_to(array[i], DOWN*5)
                indices[i].next_to(array_count[i], UP).set_color(BLUE).scale(0.9)
                self.play(Write(a), Write(indices[i]))


        counting_label = Tex("Contador:").scale(0.8)
        counting_label.next_to(array_count[0], LEFT)
        self.play(Write(counting_label))

        for a, n in zip(array_count, numbers_count):
            n.set_x(a.get_x())
            n.set_y(a.get_y())
            self.add(n)
        self.wait()

        self.wait(12)
        arrow = SVGMobject("arrow.svg").scale(0.5).rotate(PI)

        arrow.scale(0.5).next_to(numbers[0], DOWN)
        arrow[0].set_style(fill_opacity=1,stroke_width=2,fill_color=WHITE).set_stroke(color=BLACK)
        self.play(FadeIn(arrow))
        self.wait(3)

        count_um_1 = Tex("1").set_x(numbers_count[0].get_x()).set_y(numbers_count[0].get_y()).set_color(YELLOW)
        self.play(
            Transform(numbers_count[0], count_um_1)
        )
        self.wait(3)

        self.play(arrow.animate.next_to(numbers[1], DOWN))
        self.wait(3)

        count_quatro_1 = Tex("1").set_x(numbers_count[3].get_x()).set_y(numbers_count[3].get_y()).set_color(YELLOW)
        self.play(
            count_um_1.animate.set_color(WHITE),
            Transform(numbers_count[3], count_quatro_1)
        )
        self.wait(3)

        self.play(arrow.animate.next_to(numbers[2], DOWN))
        self.wait(3)

        count_um_2 = Tex("2").set_x(numbers_count[0].get_x()).set_y(numbers_count[0].get_y()).set_color(YELLOW)
        self.play(
            FadeOut(numbers_count[0]),
            count_quatro_1.animate.set_color(WHITE),
            Transform(count_um_1, count_um_2)
        )
        self.wait(3)

        self.play(arrow.animate.next_to(numbers[3], DOWN))

        count_dois_1 = Tex("1").set_x(numbers_count[1].get_x()).set_y(numbers_count[1].get_y()).set_color(YELLOW)
        self.play(
            count_um_2.animate.set_color(WHITE),
            Transform(numbers_count[1], count_dois_1)
        )

        self.play(arrow.animate.next_to(numbers[4], DOWN))

        count_sete_1 = Tex("1").set_x(numbers_count[6].get_x()).set_y(numbers_count[6].get_y()).set_color(YELLOW)
        self.play(
            count_dois_1.animate.set_color(WHITE),
            Transform(numbers_count[6], count_sete_1)
        )

        self.play(arrow.animate.next_to(numbers[5], DOWN))

        count_cinco_1 = Tex("1").set_x(numbers_count[4].get_x()).set_y(numbers_count[4].get_y()).set_color(YELLOW)
        self.play(
            count_sete_1.animate.set_color(WHITE),
            Transform(numbers_count[4], count_cinco_1)
        )

        self.play(arrow.animate.next_to(numbers[6], DOWN))

        count_dois_2 = Tex("2").set_x(numbers_count[1].get_x()).set_y(numbers_count[1].get_y()).set_color(YELLOW)
        self.play(
            FadeOut(numbers_count[1]),
            count_cinco_1.animate.set_color(WHITE),
            Transform(count_dois_1, count_dois_2)
        )
        self.wait(1)
        self.play(count_dois_2.animate.set_color(WHITE))
        count_dois_2.set_color(WHITE)
        self.wait(1.5)

        self.remove(numbers_count[0], numbers_count[1], count_um_1, count_um_2, numbers_count[3], numbers_count[4], numbers_count[6], numbers_count[1])

        self.play(
            count_sete_1.animate.shift(UP*0.5), count_cinco_1.animate.shift(UP*0.5),
            count_dois_1.animate.shift(UP*0.5), count_dois_2.animate.shift(UP*0.5),
            count_quatro_1.animate.shift(UP*0.5), count_um_2.animate.shift(UP*0.5),

            array[0].animate.shift(UP*0.5), array[1].animate.shift(UP*0.5),
            array[2].animate.shift(UP*0.5), array[3].animate.shift(UP*0.5),
            array[4].animate.shift(UP*0.5), array[5].animate.shift(UP*0.5),
            array[6].animate.shift(UP*0.5),
            numbers[0].animate.shift(UP*0.5), numbers[1].animate.shift(UP*0.5),
            numbers[2].animate.shift(UP*0.5), numbers[3].animate.shift(UP*0.5),
            numbers[4].animate.shift(UP*0.5), numbers[5].animate.shift(UP*0.5),
            numbers[6].animate.shift(UP*0.5),

            vector_label.animate.shift(UP*0.5),

            array_count[0].animate.shift(UP*0.5), array_count[1].animate.shift(UP*0.5),
            array_count[2].animate.shift(UP*0.5), array_count[3].animate.shift(UP*0.5),
            array_count[4].animate.shift(UP*0.5), array_count[5].animate.shift(UP*0.5),
            array_count[6].animate.shift(UP*0.5),

            indices[0].animate.shift(UP*0.5), indices[1].animate.shift(UP*0.5),
            indices[2].animate.shift(UP*0.5), indices[3].animate.shift(UP*0.5),
            indices[4].animate.shift(UP*0.5), indices[5].animate.shift(UP*0.5),
            indices[6].animate.shift(UP*0.5),

            numbers_count[2].animate.shift(UP*0.5), numbers_count[5].animate.shift(UP*0.5),
            vector_label.animate.shift(UP*0.5), counting_label.animate.shift(UP*0.5),
            Uncreate(arrow)
        )
        self.wait(1)
        self.play(FadeOut(count_dois_1))

        line1 = Line((0,0,0), (0,0.7,0)).set_x(array_count[0].get_x()).set_y(array_count[0].get_y() - array_count[0].get_height() + 0.15)
        line2 = Line((2,0,0), (2,0.7,0)).set_x(array_count[1].get_x()).set_y(array_count[1].get_y() - array_count[1].get_height() + 0.15)
        line3 = Line((0,0.7,0), (1.1,0.7,0)).set_x(line1.get_x() + 0.54).set_y(line1.get_y() - 0.34)
        soma = Tex("2 + 2 =").next_to(line3, DOWN)
        count_quatro_2 = Tex("4").set_x(count_dois_2.get_x()).set_y(count_dois_2.get_y()).set_color(YELLOW)
        self.play(
            ShowCreation(line1), ShowCreation(line2), ShowCreation(line3),
            Write(soma),
        )
        self.wait()
        self.play(Transform(count_dois_2, count_quatro_2))
        self.remove(count_dois_2)

        soma2 = Tex("4 + 0 =").next_to(soma, RIGHT).shift(0.63*LEFT)

        count_dois_4 = Tex("4").set_x(numbers_count[2].get_x()).set_y(numbers_count[2].get_y()).set_color(YELLOW)
        self.play(
            line1.animate.shift(RIGHT*1.1), line2.animate.shift(RIGHT*1.1),
            line3.animate.shift(RIGHT*1.1), count_quatro_2.animate.set_color(WHITE),
            ReplacementTransform(soma, soma2),
        )
        self.wait()
        self.play(ReplacementTransform(numbers_count[2], count_dois_4))

        soma = Tex("4 + 1 =").next_to(soma2, RIGHT).shift(0.63*LEFT)

        count_tres_5 = Tex("5").set_x(count_quatro_1.get_x()).set_y(count_quatro_1.get_y()).set_color(YELLOW)
        self.play(
            line1.animate.shift(RIGHT*1.1), line2.animate.shift(RIGHT*1.1),
            line3.animate.shift(RIGHT*1.1),
            count_dois_4.animate.set_color(WHITE),
            ReplacementTransform(soma2, soma),
        )
        self.play(ReplacementTransform(count_quatro_1, count_tres_5))

        soma2 = Tex("5 + 1 =").next_to(soma, RIGHT).shift(0.63*LEFT)

        count_quatro_5 = Tex("6").set_x(count_cinco_1.get_x()).set_y(count_cinco_1.get_y()).set_color(YELLOW)
        self.play(
            line1.animate.shift(RIGHT*1.1), line2.animate.shift(RIGHT*1.1),
            line3.animate.shift(RIGHT*1.1),
            count_tres_5.animate.set_color(WHITE),
            ReplacementTransform(soma, soma2),
        )
        self.play(ReplacementTransform(count_cinco_1, count_quatro_5))

        soma = Tex("6 + 0 =").next_to(soma2, RIGHT).shift(0.63*LEFT)

        count_cinco_6 = Tex("6").set_x(numbers_count[5].get_x()).set_y(numbers_count[5].get_y()).set_color(YELLOW)
        self.play(
            line1.animate.shift(RIGHT*1.1), line2.animate.shift(RIGHT*1.1),
            line3.animate.shift(RIGHT*1.1),
            ReplacementTransform(soma2, soma),
            count_quatro_5.animate.set_color(WHITE)
        )
        self.play(ReplacementTransform(numbers_count[5], count_cinco_6))

        soma2 = Tex("6 + 1 =").next_to(soma, RIGHT).shift(0.63*LEFT)

        count_seis_7 = Tex("7").set_x(count_sete_1.get_x()).set_y(count_sete_1.get_y()).set_color(YELLOW)
        self.play(
            line1.animate.shift(RIGHT*1.1), line2.animate.shift(RIGHT*1.1),
            line3.animate.shift(RIGHT*1.1),
            count_cinco_6.animate.set_color(WHITE),
            ReplacementTransform(soma, soma2),
        )
        self.play(ReplacementTransform(count_sete_1, count_seis_7))

        self.play(
            Uncreate(line1), Uncreate(line2), Uncreate(line3),
            Uncreate(soma), Uncreate(soma2),
            count_seis_7.animate.set_color(WHITE)
        )
        self.wait(3)

        self.play(
            array[0].animate.shift(UP*0.5), array[1].animate.shift(UP*0.5),
            array[2].animate.shift(UP*0.5), array[3].animate.shift(UP*0.5),
            array[4].animate.shift(UP*0.5), array[5].animate.shift(UP*0.5),
            array[6].animate.shift(UP*0.5),
            numbers[0].animate.shift(UP*0.5), numbers[1].animate.shift(UP*0.5),
            numbers[2].animate.shift(UP*0.5), numbers[3].animate.shift(UP*0.5),
            numbers[4].animate.shift(UP*0.5), numbers[5].animate.shift(UP*0.5),
            numbers[6].animate.shift(UP*0.5),

            vector_label.animate.shift(UP*0.5),

            array_count[0].animate.shift(UP*0.5), array_count[1].animate.shift(UP*0.5),
            array_count[2].animate.shift(UP*0.5), array_count[3].animate.shift(UP*0.5),
            array_count[4].animate.shift(UP*0.5), array_count[5].animate.shift(UP*0.5),
            array_count[6].animate.shift(UP*0.5),

            indices[0].animate.shift(UP*0.5), indices[1].animate.shift(UP*0.5),
            indices[2].animate.shift(UP*0.5), indices[3].animate.shift(UP*0.5),
            indices[4].animate.shift(UP*0.5), indices[5].animate.shift(UP*0.5),
            indices[6].animate.shift(UP*0.5),

            count_seis_7.animate.shift(UP*0.5), count_cinco_6.animate.shift(UP*0.5),
            count_quatro_5.animate.shift(UP*0.5), count_tres_5.animate.shift(UP*0.5),
            count_dois_4.animate.shift(UP*0.5), count_quatro_2.animate.shift(UP*0.5),
            count_um_2.animate.shift(UP*0.5),

            vector_label.animate.shift(UP*0.5), counting_label.animate.shift(UP*0.5),
        )

        array_final = VGroup(
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1)
        ).arrange(RIGHT, buff=0.1)

        numbers_final = VGroup(
            Tex("1"), Tex("4"), Tex("1"), Tex("2"),
            Tex("7"), Tex("5"), Tex("2")
        )

        for i, a in enumerate(array_final):
            a.next_to(array[i], DOWN*13)

        self.play(Write(array_final), run_time=2.5)

        vector_label_final = Tex("Vetor final:", isolate=["Vetor", "final:"]).scale(0.8)
        vector_label_final.next_to(array_final[0], LEFT)
        vector_label_final[0].shift(LEFT*0.1)
        self.play(Write(vector_label_final))
        self.wait(1)

        trash = []
        indices_final = []
        numbers_final = []

        arrow = SVGMobject("arrow.svg").scale(0.3).rotate(PI)
        arrow[0].set_style(fill_opacity=1,stroke_width=2,fill_color=WHITE).set_stroke(color=BLACK)
        arrow.next_to(array[0], DOWN*0.1).shift(0.3*UP)

        self.play(ShowCreation(arrow))
        self.wait(2)

        self.play(
            numbers[0].animate.set_color(YELLOW),
            arrow.animate.next_to(array_count[0], DOWN*0.1).shift(0.3*UP)
        )
        self.wait(2.5)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_um_2))
        )

        indices_final.append(count_um_2.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[1], UP).set_color(BLUE).scale(0.9)
        )
        self.wait(3)

        i_1 = Tex("1").set_x(count_um_2.get_x()).set_y(count_um_2.get_y()).set_color(YELLOW)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[0]))
        )

        numbers_final.append(numbers[0].copy())
        self.play(
            numbers_final[-1].animate.move_to(array_final[1]).set_color(WHITE),
            numbers[0].animate.set_color(WHITE),
        )
        self.wait()

        self.play(
            ReplacementTransform(count_um_2, i_1)
        )

        self.wait(3)

        ##DAQUI

        self.play(
            arrow.animate.next_to(array[1], DOWN*0.1).shift(0.3*UP),
            i_1.animate.set_color(WHITE)
        )
        self.wait(2)

        self.play(
            numbers[1].animate.set_color(YELLOW),
            arrow.animate.next_to(array_count[3], DOWN*0.1).shift(0.3*UP)
        )
        self.wait(3)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_tres_5))
        )

        indices_final.append(count_tres_5.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[4], UP).set_color(BLUE).scale(0.9)
        )
        trash.append(Tex("4").set_x(count_tres_5.get_x()).set_y(count_tres_5.get_y()).set_color(YELLOW))
        #self.wait(3)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[1]))
        )

        numbers_final.append(numbers[1].copy())
        self.play(
            numbers[1].animate.set_color(WHITE),
            numbers_final[-1].animate.move_to(array_final[4]).set_color(WHITE)
        )
        self.play(
            ReplacementTransform(count_tres_5, trash[-1])
        )
        self.wait(5.5)

        ##DAQUI 2

        self.play(
            arrow.animate.next_to(array[2], DOWN*0.1).shift(0.3*UP),
            trash[-1].animate.set_color(WHITE)
        )
        self.wait()

        self.play(
            numbers[2].animate.set_color(YELLOW),
            arrow.animate.next_to(array_count[0], DOWN*0.1).shift(0.3*UP)
        )
        #self.wait(2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_um_2))
        )
        indices_final.append(count_um_2.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[0], UP).set_color(BLUE).scale(0.9)
        )
        trash.append(Tex("0").set_x(count_um_2.get_x()).set_y(count_um_2.get_y()).set_color(YELLOW))
        #self.wait(3)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[2]))
        )

        numbers_final.append(numbers[2].copy())
        self.play(
            numbers_final[-1].animate.move_to(array_final[0]).set_color(WHITE),
        )
        self.wait(2)

        self.play(
            numbers[2].animate.set_color(WHITE),
        )
        self.play(ReplacementTransform(i_1, trash[-1]))
        self.wait()

        ##DAQUI 3

        self.play(
            trash[-1].animate.set_color(WHITE),
            arrow.animate.next_to(array[3], DOWN*0.1).shift(0.3*UP)
        )

        self.play(
            numbers[3].animate.set_color(YELLOW),
            arrow.animate.next_to(array_count[1], DOWN*0.1).shift(0.3*UP)
        )
        #self.wait(2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_quatro_2))
        )

        indices_final.append(count_quatro_2.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[3], UP).set_color(BLUE).scale(0.9)
        )
        i_2 = Tex("3").set_x(count_quatro_2.get_x()).set_y(count_quatro_2.get_y()).set_color(YELLOW)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[3]))
        )

        numbers_final.append(numbers[3].copy())
        self.play(
            numbers_final[-1].animate.move_to(array_final[3]).set_color(WHITE),
            numbers[3].animate.set_color(WHITE),
        )

        self.play(ReplacementTransform(count_quatro_2, i_2))

        ##DAQUI 4

        self.play(
            arrow.animate.next_to(array[4], DOWN*0.1).shift(0.3*UP),
            i_2.animate.set_color(WHITE)
        )
        self.play(
            numbers[4].animate.set_color(YELLOW),
            arrow.animate.next_to(array_count[6], DOWN*0.1).shift(0.3*UP),
        )

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_seis_7))
        )

        indices_final.append(count_seis_7.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[6], UP).set_color(BLUE).scale(0.9)
        )
        trash.append(Tex("6").set_x(count_seis_7.get_x()).set_y(count_seis_7.get_y()).set_color(YELLOW))

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[4]))
        )

        numbers_final.append(numbers[4].copy())
        self.play(
            numbers_final[-1].animate.move_to(array_final[6]).set_color(WHITE),
            numbers[4].animate.set_color(WHITE),
        )

        self.play(
            ReplacementTransform(count_seis_7, trash[-1])
        )

        ##DAQUI 5

        self.play(
            arrow.animate.next_to(array[5], DOWN*0.1).shift(0.3*UP),
            trash[-1].animate.set_color(WHITE)
        )

        self.play(
            numbers[5].animate.set_color(YELLOW),
            arrow.animate.next_to(count_quatro_5, DOWN*0.1)
        )

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_quatro_5))
        )

        indices_final.append(count_quatro_5.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[5], UP).set_color(BLUE).scale(0.9)
        )
        trash.append(Tex("5").set_x(count_quatro_5.get_x()).set_y(count_quatro_5.get_y()).set_color(YELLOW))

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[5]))
        )

        numbers_final.append(numbers[5].copy())
        self.play(
            numbers_final[-1].animate.move_to(array_final[5]).set_color(WHITE),
            numbers[5].animate.set_color(WHITE)
        )
        self.play(
            ReplacementTransform(count_quatro_5, trash[-1])
        )

        ##DAQUI 6

        self.play(
            trash[-1].animate.set_color(WHITE),
            arrow.animate.next_to(array[6], DOWN*0.1).shift(0.3*UP)
        )

        self.play(
            numbers[6].animate.set_color(YELLOW),
            arrow.animate.next_to(count_quatro_2, DOWN*0.1)
        )

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(count_quatro_2))
        )

        indices_final.append(count_quatro_2.copy())
        self.play(
            indices_final[-1].animate.next_to(array_final[2], UP).set_color(BLUE).scale(0.9)
        )
        trash.append(Tex("2").set_x(count_quatro_2.get_x()).set_y(count_quatro_2.get_y()).set_color(YELLOW))

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(numbers[6]))
        )

        numbers_final.append(numbers[6].copy())
        self.play(
            numbers_final[-1].animate.move_to(array_final[2]).set_color(WHITE),
            numbers[-1].animate.set_color(WHITE)
        )
        self.play(ReplacementTransform(i_2, trash[-1]))
        self.play(trash[-1].animate.set_color(WHITE))

        self.play(
            Uncreate(vector_label), Uncreate(array[0]), Uncreate(array[1]),
            Uncreate(array[2]), Uncreate(array[3]), Uncreate(array[4]),
            Uncreate(array[5]), Uncreate(array[6]), Uncreate(numbers[0]), Uncreate(numbers[1]),
            Uncreate(numbers[2]), Uncreate(numbers[3]), Uncreate(numbers[4]),
            Uncreate(numbers[5]), Uncreate(numbers[6]),

            Uncreate(counting_label), Uncreate(array_count[0]), Uncreate(array_count[1]),
            Uncreate(array_count[2]), Uncreate(array_count[3]), Uncreate(array_count[4]),
            Uncreate(array_count[5]), Uncreate(array_count[6]),

            Uncreate(count_cinco_6),
            Uncreate(count_dois_4),

            Uncreate(indices[0]), Uncreate(indices[1]),
            Uncreate(indices[2]), Uncreate(indices[3]), Uncreate(indices[4]),
            Uncreate(indices[5]), Uncreate(indices[6]),
            #Uncreate(i_1), Uncreate(i_2),
            Uncreate(arrow),

            Uncreate(vector_label_final),
            Uncreate(trash[0]), Uncreate(trash[1]),
            Uncreate(trash[2]), Uncreate(trash[3]),
            Uncreate(trash[4]),

            Uncreate(indices_final[0]), Uncreate(indices_final[1]),
            Uncreate(indices_final[2]), Uncreate(indices_final[3]), Uncreate(indices_final[4]),
            Uncreate(indices_final[5]), Uncreate(indices_final[6])
        )

        movement_up = UP*2.5
        self.play(
            array_final[0].animate.shift(movement_up),
            array_final[1].animate.shift(movement_up),
            array_final[2].animate.shift(movement_up),
            array_final[3].animate.shift(movement_up),
            array_final[4].animate.shift(movement_up),
            array_final[5].animate.shift(movement_up),
            array_final[6].animate.shift(movement_up),
            numbers_final[0].animate.scale(1.25).shift(movement_up),
            numbers_final[1].animate.scale(1.25).shift(movement_up),
            numbers_final[2].animate.scale(1.25).shift(movement_up),
            numbers_final[3].animate.scale(1.25).shift(movement_up),
            numbers_final[4].animate.scale(1.25).shift(movement_up),
            numbers_final[5].animate.scale(1.25).shift(movement_up),
            numbers_final[6].animate.scale(1.25).shift(movement_up),
        )
        self.wait(3)

class Cena7(Scene):
    def construct(self):
        self.wait(2)
        eq = Tex("n + k", isolate=['n', 'k']).scale(3.5)
        self.play(Write(eq), run_time=2)
        self.wait(1.6)

        self.play(eq[0].animate.set_color(BLUE))
        self.wait(0.6)
        self.play(
            eq[0].animate.set_color(WHITE),
            eq[2].animate.set_color(BLUE)
        )
        self.wait(2)
        self.play(eq[2].animate.set_color(WHITE))
        self.wait()

        self.play(eq.animate.to_edge(UP), run_time=2)
        self.wait(3)
        self.play(
            eq[0].animate.set_color(RED),
        )
        self.wait()
        self.play(
            eq[-1].animate.set_color(BLUE),
        )
        self.wait()

        eq_10_a_6=eq.copy()
        eq_10_a_6.set_x(eq.get_x()).set_y(eq.get_y())
        self.add(eq_10_a_6)
        self.play(
            eq_10_a_6.animate.shift(DOWN*2),
        )

        transf2 = Tex("10^6", color=RED).scale(2.5).set_x(eq_10_a_6[0].get_x()).set_y(eq_10_a_6[0].get_y()).shift(0.1*UP).shift(RIGHT*0.05)
        transf3 = Tex("10^6", color=BLUE).scale(2.5).set_x(eq_10_a_6[-1].get_x()).set_y(eq_10_a_6[-1].get_y()).shift(RIGHT*0.05)

        self.play(
            ReplacementTransform(eq_10_a_6[0], transf2),
            ReplacementTransform(eq_10_a_6[-1], transf3),
        )
        self.wait()

        self.play(
            eq.animate.to_edge(2.8*LEFT),
            eq_10_a_6.animate.shift(3.8*LEFT),
            transf2.animate.shift(3.8*LEFT),
            transf3.animate.shift(3.8*LEFT),
        )

        dois_milhoes = Tex("= 2 \\times 10^6 passos.", isolate=["passos."], color=WHITE).scale(2)
        dois_milhoes.next_to(eq_10_a_6, RIGHT)
        dois_milhoes[1].shift(RIGHT*0.2)
        self.play(Write(dois_milhoes))

        tempo_texto_1 = Text(
            "Dessa vez, se um computador levar meio segundo para",
            font="Arial", font_size=25,
        )

        tempo_texto_2 = Text(
            "cada operação, isso vai demorar 1 milhão de segundos",
            font="Arial", font_size=25,
            t2c={"1 milhão de segundos": RED}
        )

        tempo_texto_3 = Text(
            "para terminar, algo em torno de 11 dias.",
            font="Arial", font_size=25,
            t2c={"11 dias": RED}
        )

        a = VGroup(tempo_texto_1, tempo_texto_2, tempo_texto_3).arrange(DOWN, buff=0.2)

        tempo_texto_1.shift(DOWN*2)
        tempo_texto_2.shift(DOWN*2)
        tempo_texto_3.shift(DOWN*2)

        self.play(Write(a), run_time=1.7)

        self.wait(3)

        self.play(
            Uncreate(eq), Uncreate(eq_10_a_6),
            Uncreate(transf2), Uncreate(transf3),
            Uncreate(dois_milhoes), Uncreate(tempo_texto_1),
            Uncreate(tempo_texto_2), Uncreate(tempo_texto_3)
        )

class CenaCA(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        #self.add(background)

        ord = Text("Complexidade de Algoritmos").scale(0.96)

        self.play(Write(ord))
        self.play(Uncreate(ord))
