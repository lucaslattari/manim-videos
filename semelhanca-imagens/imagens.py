from manimlib import *
import numpy as np

class cena1imagens(Scene):
    def construct(self):
        #imagem 1
        img1 = VGroup(
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
        ).arrange(RIGHT, buff=0.1).shift(DOWN*2)
        x_img1, y_img1 = -5.5 + 0.25, 1.5
        i = 0
        for y in range(0, 4):
            for x in range(0, 4):
                img1[i].set_x(x_img1 + x).set_y(y_img1 - y)
                i += 1

        for i in range(16):
            self.play(Write(img1[i]), run_time=0.1)

        numbers_img1 = VGroup(
            Tex("39", stroke_color=BLACK, stroke_width=1),
            Tex("38", stroke_color=BLACK, stroke_width=1),
            Tex("37", stroke_color=BLACK, stroke_width=1),
            Tex("65", stroke_color=BLACK, stroke_width=1),
            Tex("66", stroke_color=BLACK, stroke_width=1),
            Tex("69", stroke_color=BLACK, stroke_width=1),
            Tex("77", stroke_color=BLACK, stroke_width=1),
            Tex("90", stroke_color=BLACK, stroke_width=1),
            Tex("91", stroke_color=BLACK, stroke_width=1),
            Tex("51", stroke_color=BLACK, stroke_width=1),
            Tex("57", stroke_color=BLACK, stroke_width=1),
            Tex("41", stroke_color=BLACK, stroke_width=1),
            Tex("44", stroke_color=BLACK, stroke_width=1),
            Tex("45", stroke_color=BLACK, stroke_width=1),
            Tex("42", stroke_color=BLACK, stroke_width=1),
            Tex("48", stroke_color=BLACK, stroke_width=1),
        )

        #imagem 2
        img2 = VGroup(
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
        ).arrange(RIGHT, buff=0.1).shift(DOWN*2)
        x_img2, y_img2 = 2.5 - 0.25, 1.5
        i = 0
        for y in range(0, 4):
            for x in range(0, 4):
                img2[i].set_x(x_img2 + x).set_y(y_img2 - y)
                i += 1

        for i in range(16):
            self.play(Write(img2[i]), run_time=0.1)

        numbers_img2 = VGroup(
            Tex("35", stroke_color=BLACK, stroke_width=1),
            Tex("11", stroke_color=BLACK, stroke_width=1),
            Tex("13", stroke_color=BLACK, stroke_width=1),
            Tex("14", stroke_color=BLACK, stroke_width=1),
            Tex("15", stroke_color=BLACK, stroke_width=1),
            Tex("12", stroke_color=BLACK, stroke_width=1),
            Tex("23", stroke_color=BLACK, stroke_width=1),
            Tex("25", stroke_color=BLACK, stroke_width=1),
            Tex("26", stroke_color=BLACK, stroke_width=1),
            Tex("29", stroke_color=BLACK, stroke_width=1),
            Tex("98", stroke_color=BLACK, stroke_width=1),
            Tex("97", stroke_color=BLACK, stroke_width=1),
            Tex("96", stroke_color=BLACK, stroke_width=1),
            Tex("94", stroke_color=BLACK, stroke_width=1),
            Tex("92", stroke_color=BLACK, stroke_width=1),
            Tex("96", stroke_color=BLACK, stroke_width=1),
        )

        gradient_list_img1 = [
            '#ff0000', '#ff0030', '#ff004f', '#ff006d',
            '#ff0089', '#ff20a3', '#f63ebc', '#e554d1',
            '#d167e4', '#b976f2', '#9f84fc', '#828fff',
            '#6299ff', '#3fa1ff', '#00a8ff', '#0093ff',
        ]

        for i in range(16):
            self.play(img1[i].animate.set_fill(gradient_list_img1[i]), run_time=0.15)

        gradient_list_img2 = [
            '#ff004f', '#44ff00', '#59ff00', '#6aff00',
            '#78ff00', '#85ff00', '#91ff00', '#9cff00',
            '#a6ff00', '#afff00', '#b9ff00', '#c2ff00',
            '#caff00', '#d2ff00', '#daff00', '#efff00',
        ]

        for i in range(16):
            self.play(img2[i].animate.set_fill(gradient_list_img2[i]), run_time=0.15)

        self.wait(1.5)

        for a, n in zip(img1, numbers_img1):
            n.set_x(a.get_x())
            n.set_y(a.get_y())
            self.add(n)

        for a, n in zip(img2, numbers_img2):
            n.set_x(a.get_x())
            n.set_y(a.get_y())
            self.add(n)

        self.wait(7)

        line1 = Line((0,0,0), (0,0.7,0), color=YELLOW).set_x(img1[0].get_x()).set_y(img1[0].get_y() + img1[0].get_height() - 0.13)
        line2 = Line((2,0,0), (2,0.7,0), color=YELLOW).set_x(img2[0].get_x()).set_y(img2[0].get_y() + img2[0].get_height() - 0.13)
        line3 = Line((0,0.7,0), (7.5,0.7,0), color=YELLOW).set_x(line1.get_x() + 3.76).set_y(line1.get_y() + 0.34)
        self.play(
            ShowCreation(line1), ShowCreation(line2), ShowCreation(line3),
        )

        self.wait(2)

        contador_label = Text("Contador de Erros = ").scale(0.5).next_to(img1, DOWN*3).shift(RIGHT*3)
        self.play(Write(contador_label))

        elements = {}

        self.wait(1.5)

        #1 iteracao
        elements["pixel1_imagem1"] = numbers_img1[0].copy()
        elements["pixel1_imagem2"] = numbers_img2[0].copy()
        elements["subtracao"] = Tex("-").next_to(line3, UP).shift(0.15*UP).shift(LEFT*0.5)
        self.play(
            elements["pixel1_imagem1"].animate.next_to(elements["subtracao"], LEFT*0.5).set_stroke(WHITE, width=0),
            elements["pixel1_imagem2"].animate.next_to(elements["subtracao"], RIGHT*0.5).set_stroke(WHITE, width=0),
            Write(elements["subtracao"])
        )
        elements["igual_eq_pixels"] = Tex("= ").next_to(elements["pixel1_imagem2"], RIGHT)
        self.play(Write(elements["igual_eq_pixels"]))
        elements["erro_30"] = Tex("4").next_to(elements["igual_eq_pixels"], RIGHT)
        self.play(Write(elements["erro_30"]))

        elements["erro_30_animacao_cima_baixo"] = elements["erro_30"].copy()
        self.play(elements["erro_30_animacao_cima_baixo"].animate.next_to(contador_label, RIGHT).shift(0.05*RIGHT))

        self.wait(2)

        self.play(
            line1.animate.shift(RIGHT),
            line2.animate.shift(RIGHT),
            line3.animate.shift(RIGHT),
            FadeOut(elements["pixel1_imagem1"]),
            FadeOut(elements["pixel1_imagem2"]),
            FadeOut(elements["subtracao"]),
            FadeOut(elements["igual_eq_pixels"]),
            FadeOut(elements["erro_30"]),
        )

        #2 iteracao
        elements["pixel2_imagem1"] = numbers_img1[1].copy()
        elements["pixel2_imagem2"] = numbers_img2[1].copy()
        elements["subtracao2"] = Tex("-").next_to(line3, UP).shift(LEFT*0.5).shift(0.15*UP)
        self.play(
            elements["pixel2_imagem1"].animate.next_to(elements["subtracao2"], LEFT*0.5).set_stroke(WHITE, width=0),
            elements["pixel2_imagem2"].animate.next_to(elements["subtracao2"], RIGHT*0.5).set_stroke(WHITE, width=0),
            Write(elements["subtracao2"])
        )
        elements["igual_eq2_pixels"] = Tex("= ").next_to(elements["pixel2_imagem2"], RIGHT)
        self.play(Write(elements["igual_eq2_pixels"]))
        elements["erro_28"] = Tex("27").next_to(elements["igual_eq2_pixels"], RIGHT)
        self.play(Write(elements["erro_28"]))

        elements["erro_28_animacao_cima_baixo"] = elements["erro_28"].copy()
        elements["soma_eq_baixo"] = Tex("+").next_to(elements["erro_30_animacao_cima_baixo"], RIGHT)
        self.play(
            Write(elements["soma_eq_baixo"]),
            elements["erro_28_animacao_cima_baixo"].animate.next_to(elements["soma_eq_baixo"], RIGHT)
        )

        self.play(
            line1.animate.shift(RIGHT),
            line2.animate.shift(RIGHT),
            line3.animate.shift(RIGHT),
            FadeOut(elements["pixel2_imagem1"]),
            FadeOut(elements["pixel2_imagem2"]),
            FadeOut(elements["subtracao2"]),
            FadeOut(elements["igual_eq2_pixels"]),
            FadeOut(elements["erro_28"]),
        )

        #3 iteracao
        elements["pixel3_imagem1"] = numbers_img1[2].copy()
        elements["pixel3_imagem2"] = numbers_img2[2].copy()
        elements["subtracao3"] = Tex("-").next_to(line3, UP).shift(LEFT*0.5).shift(0.15*UP)
        self.play(
            elements["pixel3_imagem1"].animate.next_to(elements["subtracao3"], LEFT*0.5).set_stroke(WHITE, width=0),
            elements["pixel3_imagem2"].animate.next_to(elements["subtracao3"], RIGHT*0.5).set_stroke(WHITE, width=0),
            Write(elements["subtracao3"])
        )
        elements["igual_eq3_pixels"] = Tex("= ").next_to(elements["pixel3_imagem2"], RIGHT)
        self.play(Write(elements["igual_eq3_pixels"]))
        elements["erro_14"] = Tex("24").next_to(elements["igual_eq3_pixels"], RIGHT)
        self.play(Write(elements["erro_14"]))

        elements["erro_14_animacao_cima_baixo"] = elements["erro_14"].copy()
        elements["soma_eq2_baixo"] = Tex("+").next_to(elements["erro_28_animacao_cima_baixo"], RIGHT).shift(LEFT)
        self.play(
            contador_label.animate.shift(LEFT),
            #elements["igual_eq2_pixels"].animate.shift(LEFT),
            elements["erro_30_animacao_cima_baixo"].animate.shift(LEFT),
            elements["soma_eq_baixo"].animate.shift(LEFT),
            elements["erro_28_animacao_cima_baixo"].animate.shift(LEFT),
            Write(elements["soma_eq2_baixo"]),
            elements["erro_14_animacao_cima_baixo"].animate.next_to(elements["soma_eq2_baixo"], RIGHT)
        )

        self.play(
            Uncreate(line1), Uncreate(line2), Uncreate(line3),
            Uncreate(img1), Uncreate(img2), Uncreate(contador_label),
            Uncreate(elements["erro_30_animacao_cima_baixo"]),
            Uncreate(elements["erro_28_animacao_cima_baixo"]),
            Uncreate(elements["erro_14_animacao_cima_baixo"]),
            Uncreate(elements["soma_eq_baixo"]),
            Uncreate(elements["soma_eq2_baixo"]),
            Uncreate(elements["pixel3_imagem1"]),
            Uncreate(elements["pixel3_imagem2"]),
            Uncreate(elements["subtracao3"]),
            Uncreate(numbers_img1),
            Uncreate(numbers_img2),
            Uncreate(elements["igual_eq3_pixels"]),
            Uncreate(elements["erro_14"])
        )

class labelEQM(Scene):
    def construct(self):
        background = Rectangle(
            width = 20.0,
            height = 10.0,
            stroke_width = 0,
            fill_color = "#009933",
            fill_opacity = 1
        )
        self.add(background)

        ord = Text("Erro Quadrático", stroke_width=3, stroke_color=BLACK).scale(1.5)
        ord2 = Text("Médio", stroke_width=3, stroke_color=BLACK).scale(1.5)
        g = VGroup(ord, ord2).arrange(DOWN)

        self.play(Write(g))
        self.wait(2)

        self.play(Uncreate(g))

class cena2mse(Scene):
    def construct(self):
        title = Text("Erro Quadrático Médio").scale(0.8).to_edge(UP)

        eq = Tex(
            "EQM = \\frac{1}{l \\times a} \\sum_{x=1}^{l}\\sum_{y=1}^{a} (IMAGEM_1(x,y) - IMAGEM_2(x,y))^2",
            isolate=["EQM = ", "\\frac{1}{l \\times a}", "\\sum_{x=1}^{l}", "\\sum_{y=1}^{a}", "IMAGEM_1(x,y)", "IMAGEM_2(x,y)", "^2"]
        ).scale(1)

        self.add(title)
        self.play(Write(eq[0]))
        self.wait(2.5)
        self.play(Write(eq[-5]))
        self.wait(1.6)
        self.play(Write(eq[-4]))
        self.wait()
        self.play(Write(eq[-3]))
        self.wait(2)
        self.play(
            eq[0].animate.shift(UP), #EQM=
            eq[-5].animate.shift(UP), #IMG1
            eq[-4].animate.shift(UP), #-
            eq[-3].animate.shift(UP), #IMG2
        )
        self.wait()

        img1 = VGroup(
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
        ).arrange(RIGHT, buff=0.1).shift(DOWN*2)
        x_img1, y_img1 = -5.5, 1.5
        i = 0
        for y in range(0, 4):
            for x in range(0, 4):
                img1[i].set_x(x_img1 + x).set_y(y_img1 - y)
                i += 1

        img1.scale(0.5)
        img1.next_to(eq[-5], DOWN*3)
        self.play(ShowCreation(img1))

        #animacao primeiro pixel
        temp0_x = Tex("0").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        temp0_y = Tex("0").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y()).shift(0.05*UP)
        self.play(
            ReplacementTransform(eq[-5][8], temp0_x),
            ReplacementTransform(eq[-5][10], temp0_y),
            img1[0].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp1_x = Tex("1").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        self.play(
            ReplacementTransform(temp0_x, temp1_x),
            img1[0].animate.set_fill(WHITE),
            img1[1].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp2_x = Tex("2").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        self.play(
            ReplacementTransform(temp1_x, temp2_x),
            img1[1].animate.set_fill(WHITE),
            img1[2].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp3_x = Tex("3").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        self.play(
            ReplacementTransform(temp2_x, temp3_x),
            img1[2].animate.set_fill(WHITE),
            img1[3].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp0_x = Tex("0").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        temp1_y = Tex("1").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y())
        self.play(
            ReplacementTransform(temp3_x, temp0_x),
            ReplacementTransform(temp0_y, temp1_y),
            img1[3].animate.set_fill(WHITE),
            img1[4].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp1_x = Tex("1").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        self.play(
            ReplacementTransform(temp0_x, temp1_x),
            img1[4].animate.set_fill(WHITE),
            img1[5].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp2_x = Tex("2").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        self.play(
            ReplacementTransform(temp1_x, temp2_x),
            img1[5].animate.set_fill(WHITE),
            img1[6].animate.set_fill(YELLOW),
            run_time=0.5
        )
        temp3_x = Tex("3").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        self.play(
            ReplacementTransform(temp2_x, temp3_x),
            img1[6].animate.set_fill(WHITE),
            img1[7].animate.set_fill(YELLOW),
            run_time=0.5
        )
        tex_x = Tex("x").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y())
        tex_y = Tex("y").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y())
        tex_y.shift(0.02*DOWN)

        self.play(img1[7].animate.set_fill(WHITE))
        self.play(
            FadeOut(img1),
            ReplacementTransform(temp3_x, tex_x),
            ReplacementTransform(temp1_y, tex_y),
        )
        self.wait(8.8)

        eq[2].shift(UP)
        self.play(Write(eq[2][1]))
        self.wait(2)
        self.play(eq[2][1].animate.set_color(YELLOW))
        self.wait(5)

        eq_sum = Tex("\\sum_{i=0}^2 (i-1) = (0 - 1) + (1 - 1) + (2 - 1)", isolate=['\\sum_{i=0}^2', '(i-1)', '=', '(0 - 1)', '+', '(1 - 1)']).next_to(eq, DOWN)
        sigma_temp = eq[2][1].copy()
        self.play(
            eq[2][1].animate.set_color(WHITE),
            ReplacementTransform(sigma_temp, eq_sum[0][1]),
            Write(eq_sum[0:2]),
        )
        self.wait()
        self.play(eq_sum[1].animate.set_color(YELLOW))
        self.play(
            eq_sum[1].animate.set_color(WHITE),
            eq_sum[0][2:5].animate.set_color(YELLOW),
        )
        self.wait(2.5)
        self.play(
            eq_sum[0][0].animate.set_color(YELLOW),
            eq_sum[0][2:5].animate.set_color(WHITE),
        )
        self.wait()

        temp_i_0 = eq_sum[1].copy()
        eq_sum[3][1].set_color(YELLOW)
        self.play(eq_sum[0][0].animate.set_color(WHITE))
        self.wait()
        self.play(
            eq_sum[0][2:5].animate.set_color(YELLOW),
            temp_i_0[1].animate.set_color(YELLOW)
        )
        self.play(
            Write(eq_sum[2]),
            ReplacementTransform(temp_i_0, eq_sum[3])
        )
        self.play(eq_sum[3][1].animate.set_color(WHITE))

        temp_i_1 = eq_sum[1].copy()
        eq_sum[5][1].set_color(YELLOW)
        self.play(
            eq_sum[0][2:5].animate.set_color(WHITE),
            temp_i_1[1].animate.set_color(YELLOW)
        )
        self.play(
            Write(eq_sum[4]),
            ReplacementTransform(temp_i_1, eq_sum[5])
        )
        self.play(eq_sum[5][1].animate.set_color(WHITE))
        self.wait(2)

        temp_i_2 = eq_sum[1].copy()
        eq_sum[7][1].set_color(YELLOW)
        self.play(
            eq_sum[0][0].animate.set_color(YELLOW),
            temp_i_2[1].animate.set_color(YELLOW)
        )
        self.play(
            Write(eq_sum[6]),
            ReplacementTransform(temp_i_2, eq_sum[7])
        )
        self.play(
            eq_sum[0][0].animate.set_color(WHITE),
            eq_sum[7][1].animate.set_color(WHITE)
        )
        self.wait(2)

        self.play(
            Uncreate(eq_sum),
        )

        self.wait(6)

        self.play(
            Write(eq[2][0]),
            Write(eq[2][2:5]),
        )
        self.play(eq[2].animate.set_color(YELLOW))
        self.wait(2)

        img2 = VGroup(
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
                Square(color=WHITE, stroke_color=BLACK, fill_opacity=1, side_length=1),
        ).arrange(RIGHT, buff=0.1).shift(DOWN*2)
        x_img, y_img = -5.5, 1.5
        i = 0
        for y in range(0, 4):
            for x in range(0, 4):
                img2[i].set_x(x_img + x).set_y(y_img - y)
                i += 1

        img2.scale(0.5)
        img2.next_to(eq[-3], DOWN*3)

        label_img1_x1 = Text('1').scale(0.3).next_to(img1[0], UP)
        label_img1_x2 = Text('2').scale(0.3).next_to(img1[1], UP)
        label_img1_x3 = Text('3').scale(0.3).next_to(img1[2], UP)
        label_img1_x4 = Text('l=4').scale(0.3).next_to(img1[3], UP)
        label_img2_x1 = Text('1').scale(0.3).next_to(img2[0], UP)
        label_img2_x2 = Text('2').scale(0.3).next_to(img2[1], UP)
        label_img2_x3 = Text('3').scale(0.3).next_to(img2[2], UP)
        label_img2_x4 = Text('l=4').scale(0.3).next_to(img2[3], UP)
        self.play(
            FadeIn(img1),
            Write(label_img1_x1), Write(label_img1_x2),
            Write(label_img1_x3), Write(label_img1_x4),
            Write(label_img2_x1), Write(label_img2_x2),
            Write(label_img2_x3), Write(label_img2_x4),
            ShowCreation(img2),
        )
        self.wait(8)
        self.play(
            tex_x.animate.set_color(YELLOW),
            eq[-3][8].animate.set_color(YELLOW),
            label_img1_x1.animate.set_color(YELLOW),
            img1[0].animate.set_fill(YELLOW),
            img1[4].animate.set_fill(YELLOW),
            img1[8].animate.set_fill(YELLOW),
            img1[12].animate.set_fill(YELLOW),
            label_img2_x1.animate.set_color(YELLOW),
            img2[0].animate.set_fill(YELLOW),
            img2[4].animate.set_fill(YELLOW),
            img2[8].animate.set_fill(YELLOW),
            img2[12].animate.set_fill(YELLOW),
            run_time=0.5,
        )
        self.play(
            label_img1_x1.animate.set_color(WHITE),
            img1[0].animate.set_fill(WHITE),
            img1[4].animate.set_fill(WHITE),
            img1[8].animate.set_fill(WHITE),
            img1[12].animate.set_fill(WHITE),
            label_img2_x1.animate.set_color(WHITE),
            img2[0].animate.set_fill(WHITE),
            img2[4].animate.set_fill(WHITE),
            img2[8].animate.set_fill(WHITE),
            img2[12].animate.set_fill(WHITE),

            label_img1_x2.animate.set_color(YELLOW),
            img1[1].animate.set_fill(YELLOW),
            img1[5].animate.set_fill(YELLOW),
            img1[9].animate.set_fill(YELLOW),
            img1[13].animate.set_fill(YELLOW),
            label_img2_x2.animate.set_color(YELLOW),
            img2[1].animate.set_fill(YELLOW),
            img2[5].animate.set_fill(YELLOW),
            img2[9].animate.set_fill(YELLOW),
            img2[13].animate.set_fill(YELLOW),
            run_time=0.5,
        )
        self.play(
            label_img1_x2.animate.set_color(WHITE),
            img1[1].animate.set_fill(WHITE),
            img1[5].animate.set_fill(WHITE),
            img1[9].animate.set_fill(WHITE),
            img1[13].animate.set_fill(WHITE),
            label_img2_x2.animate.set_color(WHITE),
            img2[1].animate.set_fill(WHITE),
            img2[5].animate.set_fill(WHITE),
            img2[9].animate.set_fill(WHITE),
            img2[13].animate.set_fill(WHITE),

            label_img1_x3.animate.set_color(YELLOW),
            img1[2].animate.set_fill(YELLOW),
            img1[6].animate.set_fill(YELLOW),
            img1[10].animate.set_fill(YELLOW),
            img1[14].animate.set_fill(YELLOW),
            label_img2_x3.animate.set_color(YELLOW),
            img2[2].animate.set_fill(YELLOW),
            img2[6].animate.set_fill(YELLOW),
            img2[10].animate.set_fill(YELLOW),
            img2[14].animate.set_fill(YELLOW),
            run_time=0.5,
        )
        self.play(
            label_img1_x3.animate.set_color(WHITE),
            img1[2].animate.set_fill(WHITE),
            img1[6].animate.set_fill(WHITE),
            img1[10].animate.set_fill(WHITE),
            img1[14].animate.set_fill(WHITE),
            label_img2_x3.animate.set_color(WHITE),
            img2[2].animate.set_fill(WHITE),
            img2[6].animate.set_fill(WHITE),
            img2[10].animate.set_fill(WHITE),
            img2[14].animate.set_fill(WHITE),

            label_img1_x4.animate.set_color(YELLOW),
            img1[3].animate.set_fill(YELLOW),
            img1[7].animate.set_fill(YELLOW),
            img1[11].animate.set_fill(YELLOW),
            img1[15].animate.set_fill(YELLOW),
            label_img2_x4.animate.set_color(YELLOW),
            img2[3].animate.set_fill(YELLOW),
            img2[7].animate.set_fill(YELLOW),
            img2[11].animate.set_fill(YELLOW),
            img2[15].animate.set_fill(YELLOW),
            run_time=0.5,
        )
        self.play(
            label_img1_x4.animate.set_color(WHITE),
            img1[3].animate.set_fill(WHITE),
            img1[7].animate.set_fill(WHITE),
            img1[11].animate.set_fill(WHITE),
            img1[15].animate.set_fill(WHITE),
            label_img2_x4.animate.set_color(WHITE),
            img2[3].animate.set_fill(WHITE),
            img2[7].animate.set_fill(WHITE),
            img2[11].animate.set_fill(WHITE),
            img2[15].animate.set_fill(WHITE),
            tex_x.animate.set_color(WHITE),
            eq[-3][8].animate.set_color(WHITE),
            eq[2].animate.set_color(WHITE),
            run_time=0.5,
        )
        self.play(
            eq[2][2:5].animate.set_color(YELLOW)
        )
        self.play(
            eq[2][2:5].animate.set_color(WHITE),
            eq[2][0].animate.set_color(YELLOW)
        )
        self.play(
            eq[2][0].animate.set_color(WHITE)
        )
        self.wait()

        label_img1_y1 = Text('1').scale(0.3).next_to(img1[0], LEFT)
        label_img1_y2 = Text('2').scale(0.3).next_to(img1[4], LEFT)
        label_img1_y3 = Text('3').scale(0.3).next_to(img1[8], LEFT)
        label_img1_y4 = Text('a=4').scale(0.3).next_to(img1[12], LEFT)
        label_img2_y1 = Text('1').scale(0.3).next_to(img2[0], LEFT)
        label_img2_y2 = Text('2').scale(0.3).next_to(img2[4], LEFT)
        label_img2_y3 = Text('3').scale(0.3).next_to(img2[8], LEFT)
        label_img2_y4 = Text('a=4').scale(0.3).next_to(img2[12], LEFT)
        eq[3].shift(UP)
        self.play(
            Write(eq[3]), Write(label_img1_y1),
            Write(label_img1_y2), Write(label_img1_y3),
            Write(label_img1_y4), Write(label_img2_y1),
            Write(label_img2_y2), Write(label_img2_y3),
            Write(label_img2_y4),
        )
        self.play(
            eq[3].animate.set_color(YELLOW)
        )

        self.wait(0.8)
        self.play(
            eq[-3][10].animate.set_color(YELLOW),
            tex_y.animate.set_color(YELLOW),
            label_img1_y1.animate.set_color(YELLOW),
            img1[0].animate.set_fill(YELLOW),
            img1[1].animate.set_fill(YELLOW),
            img1[2].animate.set_fill(YELLOW),
            img1[3].animate.set_fill(YELLOW),
            label_img2_y1.animate.set_color(YELLOW),
            img2[0].animate.set_fill(YELLOW),
            img2[1].animate.set_fill(YELLOW),
            img2[2].animate.set_fill(YELLOW),
            img2[3].animate.set_fill(YELLOW),
            run_time=0.45,
        )
        self.play(
            label_img1_y1.animate.set_color(WHITE),
            img1[0].animate.set_fill(WHITE),
            img1[1].animate.set_fill(WHITE),
            img1[2].animate.set_fill(WHITE),
            img1[3].animate.set_fill(WHITE),
            label_img2_y1.animate.set_color(WHITE),
            img2[0].animate.set_fill(WHITE),
            img2[1].animate.set_fill(WHITE),
            img2[2].animate.set_fill(WHITE),
            img2[3].animate.set_fill(WHITE),

            label_img1_y2.animate.set_color(YELLOW),
            img1[4].animate.set_fill(YELLOW),
            img1[5].animate.set_fill(YELLOW),
            img1[6].animate.set_fill(YELLOW),
            img1[7].animate.set_fill(YELLOW),
            label_img2_y2.animate.set_color(YELLOW),
            img2[4].animate.set_fill(YELLOW),
            img2[5].animate.set_fill(YELLOW),
            img2[6].animate.set_fill(YELLOW),
            img2[7].animate.set_fill(YELLOW),
            run_time=0.45,
        )
        self.play(
            label_img1_y2.animate.set_color(WHITE),
            img1[4].animate.set_fill(WHITE),
            img1[5].animate.set_fill(WHITE),
            img1[6].animate.set_fill(WHITE),
            img1[7].animate.set_fill(WHITE),
            label_img2_y2.animate.set_color(WHITE),
            img2[4].animate.set_fill(WHITE),
            img2[5].animate.set_fill(WHITE),
            img2[6].animate.set_fill(WHITE),
            img2[7].animate.set_fill(WHITE),

            label_img1_y3.animate.set_color(YELLOW),
            img1[8].animate.set_fill(YELLOW),
            img1[9].animate.set_fill(YELLOW),
            img1[10].animate.set_fill(YELLOW),
            img1[11].animate.set_fill(YELLOW),
            label_img2_y3.animate.set_color(YELLOW),
            img2[8].animate.set_fill(YELLOW),
            img2[9].animate.set_fill(YELLOW),
            img2[10].animate.set_fill(YELLOW),
            img2[11].animate.set_fill(YELLOW),
            run_time=0.45,
        )
        self.play(
            label_img1_y3.animate.set_color(WHITE),
            img1[8].animate.set_fill(WHITE),
            img1[9].animate.set_fill(WHITE),
            img1[10].animate.set_fill(WHITE),
            img1[11].animate.set_fill(WHITE),
            label_img2_y3.animate.set_color(WHITE),
            img2[8].animate.set_fill(WHITE),
            img2[9].animate.set_fill(WHITE),
            img2[10].animate.set_fill(WHITE),
            img2[11].animate.set_fill(WHITE),

            label_img1_y4.animate.set_color(YELLOW),
            img1[12].animate.set_fill(YELLOW),
            img1[13].animate.set_fill(YELLOW),
            img1[14].animate.set_fill(YELLOW),
            img1[15].animate.set_fill(YELLOW),
            label_img2_y4.animate.set_color(YELLOW),
            img2[12].animate.set_fill(YELLOW),
            img2[13].animate.set_fill(YELLOW),
            img2[14].animate.set_fill(YELLOW),
            img2[15].animate.set_fill(YELLOW),
            run_time=0.45,
        )
        self.play(
            label_img1_y4.animate.set_color(WHITE),
            img1[12].animate.set_fill(WHITE),
            img1[13].animate.set_fill(WHITE),
            img1[14].animate.set_fill(WHITE),
            img1[15].animate.set_fill(WHITE),
            label_img2_y4.animate.set_color(WHITE),
            img2[12].animate.set_fill(WHITE),
            img2[13].animate.set_fill(WHITE),
            img2[14].animate.set_fill(WHITE),
            img2[15].animate.set_fill(WHITE),
            eq[-3][10].animate.set_color(WHITE),
            tex_y.animate.set_color(WHITE),
            eq[3].animate.set_color(WHITE),
            run_time=0.45,
        )
        self.play(
            eq[3][2:5].animate.set_color(YELLOW),
            run_time=0.6,
        )
        self.play(
            eq[3][2:5].animate.set_color(WHITE),
            eq[3][0].animate.set_color(YELLOW),
            run_time=0.6,
        )
        self.play(
            eq[3][0].animate.set_color(WHITE),
            run_time=0.6,
        )

        tex_x_img1 = Tex("1").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_y_img1 = Tex("1").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("1").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        tex_y_img2 = Tex("1").set_x(eq[-3][10].get_x()).set_y(eq[-3][10].get_y()).set_color(YELLOW)
        tex_y_img2.shift(0.05*UP)

        self.play(
            img1[0].animate.set_fill(YELLOW),
            img2[0].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x, tex_x_img1),
            ReplacementTransform(tex_y, tex_y_img1),
            ReplacementTransform(eq[-3][8], tex_x_img2),
            ReplacementTransform(eq[-3][10], tex_y_img2),
            run_time=0.4,
        )
        self.wait()

        tex_x1_img1 = Tex("2").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x1_img2 = Tex("2").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)

        self.play(
            img1[0].animate.set_fill(WHITE),
            img2[0].animate.set_fill(WHITE),
            img1[1].animate.set_fill(YELLOW),
            img2[1].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x1_img1),
            ReplacementTransform(tex_x_img2, tex_x1_img2),
            run_time=0.4,
        )

        tex_x_img1 = Tex("3").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("3").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[1].animate.set_fill(WHITE),
            img2[1].animate.set_fill(WHITE),
            img1[2].animate.set_fill(YELLOW),
            img2[2].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x1_img1, tex_x_img1),
            ReplacementTransform(tex_x1_img2, tex_x_img2),
            run_time=0.4,
        )

        tex_x3_img1 = Tex("4").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x3_img2 = Tex("4").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[2].animate.set_fill(WHITE),
            img2[2].animate.set_fill(WHITE),
            img1[3].animate.set_fill(YELLOW),
            img2[3].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x3_img1),
            ReplacementTransform(tex_x_img2, tex_x3_img2),
            run_time=0.4,
        )

        tex_x_img1 = Tex("1").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("1").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        tex_y2_img1 = Tex("2").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y()).set_color(YELLOW)
        tex_y2_img2 = Tex("2").set_x(eq[-3][10].get_x()).set_y(eq[-3][10].get_y()).set_color(YELLOW)
        self.play(
            img1[3].animate.set_fill(WHITE),
            img2[3].animate.set_fill(WHITE),
            img1[4].animate.set_fill(YELLOW),
            img2[4].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x3_img1, tex_x_img1),
            ReplacementTransform(tex_x3_img2, tex_x_img2),
            ReplacementTransform(tex_y_img1, tex_y2_img1),
            ReplacementTransform(tex_y_img2, tex_y2_img2),
            run_time=0.4,
        )

        tex_x1_img1 = Tex("2").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x1_img2 = Tex("2").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[4].animate.set_fill(WHITE),
            img2[4].animate.set_fill(WHITE),
            img1[5].animate.set_fill(YELLOW),
            img2[5].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x1_img1),
            ReplacementTransform(tex_x_img2, tex_x1_img2),
            run_time=0.4,
        )

        tex_x_img1 = Tex("3").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("3").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[5].animate.set_fill(WHITE),
            img2[5].animate.set_fill(WHITE),
            img1[6].animate.set_fill(YELLOW),
            img2[6].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x1_img1, tex_x_img1),
            ReplacementTransform(tex_x1_img2, tex_x_img2),
            run_time=0.4,
        )

        tex_x3_img1 = Tex("4").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x3_img2 = Tex("4").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[6].animate.set_fill(WHITE),
            img2[6].animate.set_fill(WHITE),
            img1[7].animate.set_fill(YELLOW),
            img2[7].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x3_img1),
            ReplacementTransform(tex_x_img2, tex_x3_img2),
            run_time=0.4,
        )

        ###################################################
        tex_x_img1 = Tex("1").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("1").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        tex_y_img1 = Tex("3").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y()).set_color(YELLOW)
        tex_y_img2 = Tex("3").set_x(eq[-3][10].get_x()).set_y(eq[-3][10].get_y()).set_color(YELLOW)
        self.play(
            img1[7].animate.set_fill(WHITE),
            img2[7].animate.set_fill(WHITE),
            img1[8].animate.set_fill(YELLOW),
            img2[8].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x3_img1, tex_x_img1),
            ReplacementTransform(tex_x3_img2, tex_x_img2),
            ReplacementTransform(tex_y2_img1, tex_y_img1),
            ReplacementTransform(tex_y2_img2, tex_y_img2),
            run_time=0.4,
        )

        tex_x1_img1 = Tex("2").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x1_img2 = Tex("2").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[8].animate.set_fill(WHITE),
            img2[8].animate.set_fill(WHITE),
            img1[9].animate.set_fill(YELLOW),
            img2[9].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x1_img1),
            ReplacementTransform(tex_x_img2, tex_x1_img2),
            run_time=0.4,
        )

        tex_x_img1 = Tex("3").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("3").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[9].animate.set_fill(WHITE),
            img2[9].animate.set_fill(WHITE),
            img1[10].animate.set_fill(YELLOW),
            img2[10].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x1_img1, tex_x_img1),
            ReplacementTransform(tex_x1_img2, tex_x_img2),
            run_time=0.4,
        )

        tex_x3_img1 = Tex("4").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x3_img2 = Tex("4").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[10].animate.set_fill(WHITE),
            img2[10].animate.set_fill(WHITE),
            img1[11].animate.set_fill(YELLOW),
            img2[11].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x3_img1),
            ReplacementTransform(tex_x_img2, tex_x3_img2),
            run_time=0.4,
        )

        ###################################################
        tex_x_img1 = Tex("1").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("1").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        tex_y4_img1 = Tex("4").set_x(eq[-5][10].get_x()).set_y(eq[-5][10].get_y()).set_color(YELLOW)
        tex_y4_img2 = Tex("4").set_x(eq[-3][10].get_x()).set_y(eq[-3][10].get_y()).set_color(YELLOW)
        self.play(
            img1[11].animate.set_fill(WHITE),
            img2[11].animate.set_fill(WHITE),
            img1[12].animate.set_fill(YELLOW),
            img2[12].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x3_img1, tex_x_img1),
            ReplacementTransform(tex_x3_img2, tex_x_img2),
            ReplacementTransform(tex_y_img1, tex_y4_img1),
            ReplacementTransform(tex_y_img2, tex_y4_img2),
            run_time=0.4,
        )

        tex_x1_img1 = Tex("2").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x1_img2 = Tex("2").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[12].animate.set_fill(WHITE),
            img2[12].animate.set_fill(WHITE),
            img1[13].animate.set_fill(YELLOW),
            img2[13].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x1_img1),
            ReplacementTransform(tex_x_img2, tex_x1_img2),
            run_time=0.4,
        )

        tex_x_img1 = Tex("3").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x_img2 = Tex("3").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[13].animate.set_fill(WHITE),
            img2[13].animate.set_fill(WHITE),
            img1[14].animate.set_fill(YELLOW),
            img2[14].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x1_img1, tex_x_img1),
            ReplacementTransform(tex_x1_img2, tex_x_img2),
            run_time=0.4,
        )

        tex_x3_img1 = Tex("4").set_x(eq[-5][8].get_x()).set_y(eq[-5][8].get_y()).set_color(YELLOW)
        tex_x3_img2 = Tex("4").set_x(eq[-3][8].get_x()).set_y(eq[-3][8].get_y()).set_color(YELLOW)
        self.play(
            img1[14].animate.set_fill(WHITE),
            img2[14].animate.set_fill(WHITE),
            img1[15].animate.set_fill(YELLOW),
            img2[15].animate.set_fill(YELLOW),
            ReplacementTransform(tex_x_img1, tex_x3_img1),
            ReplacementTransform(tex_x_img2, tex_x3_img2),
            run_time=0.4,
        )

        self.play(
            tex_x3_img1.animate.set_fill(WHITE),
            tex_x3_img2.animate.set_fill(WHITE),
            tex_y4_img1.animate.set_fill(WHITE),
            tex_y4_img2.animate.set_fill(WHITE),
            img1[15].animate.set_fill(WHITE),
            img2[15].animate.set_fill(WHITE),
            run_time=0.4,
        )

        eq[-1].set_color(YELLOW)
        self.play(
            Uncreate(img1), Uncreate(img2),
            Uncreate(label_img1_y1), Uncreate(label_img1_y2),
            Uncreate(label_img1_y3), Uncreate(label_img1_y4),
            Uncreate(label_img2_y1), Uncreate(label_img2_y2),
            Uncreate(label_img2_y3), Uncreate(label_img2_y4),
            Uncreate(label_img1_x1), Uncreate(label_img1_x2),
            Uncreate(label_img1_x3), Uncreate(label_img1_x4),
            Uncreate(label_img2_x1), Uncreate(label_img2_x2),
            Uncreate(label_img2_x3), Uncreate(label_img2_x4),
            run_time=0.5,
        )
        self.play(
            eq[0].animate.shift(DOWN),
            eq[2].animate.shift(DOWN),
            eq[3].animate.shift(DOWN),
            eq[5][:8].animate.shift(DOWN),
            eq[5][9].animate.shift(DOWN),
            eq[5][11:].animate.shift(DOWN),
            eq[6].animate.shift(DOWN),
            eq[7][:8].animate.shift(DOWN),
            eq[7][9].animate.shift(DOWN),
            eq[7][11:].animate.shift(DOWN),
            tex_x3_img1.animate.shift(DOWN),
            tex_x3_img2.animate.shift(DOWN),
            tex_y4_img1.animate.shift(DOWN),
            tex_y4_img2.animate.shift(DOWN),
        )
        self.play(
            FadeIn(eq[-1]),
            FadeIn(eq[-2]),
            FadeIn(eq[-6]),
        )

        eq[1].set_color(YELLOW)
        self.wait(3)
        self.play(
            eq[-1].animate.set_color(WHITE), FadeIn(eq[1]),
        )
        self.wait(3)
        self.play(eq[1].animate.set_color(WHITE))
        self.play(
            Uncreate(title), Uncreate(eq[0]),
            Uncreate(eq[2]), Uncreate(eq[3]),
            Uncreate(eq[5][:8]), Uncreate(eq[5][9]),
            Uncreate(eq[5][11:]), Uncreate(eq[6]),
            Uncreate(eq[7][:8]), Uncreate(eq[7][9]),
            Uncreate(eq[7][11:]), Uncreate(tex_x3_img1),
            Uncreate(tex_x3_img2), Uncreate(tex_y4_img1),
            Uncreate(tex_y4_img2), Uncreate(eq[-1]),
            Uncreate(eq[-2]), Uncreate(eq[-6]),
            Uncreate(eq[1]),
        )

class cena3bw(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        s1 = ImageMobject("sup_borda2.png").scale(0.7).shift(3.8*LEFT)
        s2 = ImageMobject("sup_borda.png").scale(0.7).shift(3.8*RIGHT)

        self.play(
            ShowCreation(s1),
            ShowCreation(s2),
        )

        s1_bw = ImageMobject("sup_borda_bw.png").scale(0.7).shift(3.8*LEFT)
        s2_bw = ImageMobject("sup_borda_bw2.png").scale(0.7).shift(3.8*RIGHT)

        self.play(
            FadeOut(s1),
            FadeOut(s2),
            FadeIn(s1_bw),
            FadeIn(s2_bw),
            run_time=0.9
        )

        self.wait(2)

        self.play(FadeOut(s1_bw), FadeOut(s2_bw))
        self.wait(2)

class cenajurassic(Scene):
    def construct(self):
        s1 = ImageMobject("jurassic.jpg").scale(1.1)

        self.play(
            FadeIn(s1),
        )

        self.wait(30)

        self.play(FadeOut(s1))
        self.wait(2)

class cena4comp(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        s1 = ImageMobject("1.jpg").scale(0.7).shift(3.8*LEFT)
        s2 = ImageMobject("2.jpg").scale(0.7).shift(3.8*RIGHT).shift(UP*2)
        s3 = ImageMobject("3.jpg").scale(0.7).shift(3.8*RIGHT).shift(DOWN*2)

        self.play(
            ShowCreation(s1),
            ShowCreation(s2),
            ShowCreation(s3),
        )
        self.wait(2)

        self.play(
            FadeOut(s1),
            FadeOut(s2),
            FadeOut(s3),
        )
        self.wait(2)

class cena5ssim(Scene):
    def construct(self):
        title = Text("Índice de Similaridade Estrutural").scale(0.65).to_edge(UP)
        self.add(title)

        eq = Tex("SSIM(I_1, I_2) = L(I_1, I_2)", isolate=['SSIM(I_1, I_2)', 'L(I_1, I_2)'])
        self.play(Write(eq[0:2]))
        self.wait(6)
        self.play(Write(eq[2]))
        self.play(eq[2].animate.set_color(YELLOW))
        self.wait(2.6)

        self.play(
            eq[2].animate.set_color(WHITE),
            eq[2][2:4].animate.set_color(YELLOW)
        )

        self.play(
            eq[2][2:4].animate.set_color(WHITE),
            eq[2][5:7].animate.set_color(YELLOW),
        )

        self.play(
            eq[2][5:7].animate.set_color(WHITE),
        )

        self.wait(2)

        eq_lum = Tex("\\frac{2 \\times \\mu_{I_1} \\times \\mu_{I_2} + C_1}{\\mu_{I_1}^2 + \\mu_{I_2}^2 + C_1}")
        self.play(
            eq[0:2].animate.shift(LEFT*3),
            ReplacementTransform(eq[2], eq_lum)
        )
        self.wait(1.5)

        self.play(
            eq_lum[0][2:5].animate.set_color(YELLOW),
            eq_lum[0][6:9].animate.set_color(YELLOW),
            eq_lum[0][13:17].animate.set_color(YELLOW),
            eq_lum[0][18:22].animate.set_color(YELLOW),
        )
        self.wait(8.5)

        self.play(
            eq_lum[0][2:5].animate.set_color(WHITE),
            eq_lum[0][6:9].animate.set_color(WHITE),
            eq_lum[0][13:17].animate.set_color(WHITE),
            eq_lum[0][18:22].animate.set_color(WHITE),

            eq_lum[0][10:12].animate.set_color(YELLOW),
            eq_lum[0][23:25].animate.set_color(YELLOW),
        )

        self.wait(2)

        self.play(
            eq_lum[0][10:12].animate.set_color(WHITE),
            eq_lum[0][23:25].animate.set_color(WHITE),
        )

        lum_or = Tex("L(I_1, I_2)").shift(LEFT*1.2)
        self.play(ReplacementTransform(eq_lum, lum_or))

        cont_eq = Tex(" \\times C(I_1, I_2)",
            isolate=["C(I_1, I_2)"]).next_to(eq_lum, RIGHT)
        cont_eq[1].shift(RIGHT*0.2)
        self.play(Write(cont_eq))
        self.wait()
        self.play(cont_eq[1:].animate.set_color(YELLOW))
        self.wait(21)

        eq_con = Tex("\\frac{2 \\times \\sigma_{I_1} \\times \\sigma_{I_2} + C_2}{\\sigma_{I_1}^2 + \\sigma_{I_2}^2}")
        eq_con.set_x(cont_eq[1].get_x()).set_y(cont_eq[1].get_y()).shift(RIGHT*1.1)
        self.play(
            ReplacementTransform(cont_eq[1], eq_con)
        )

        self.wait()
        self.play(
            eq_con[0][2:5].animate.set_color(YELLOW),
            eq_con[0][13:17].animate.set_color(YELLOW),
        )
        self.wait()

        self.play(
            eq_con[0][2:5].animate.set_color(WHITE),
            eq_con[0][13:17].animate.set_color(WHITE),

            eq_con[0][6:9].animate.set_color(YELLOW),
            eq_con[0][18:22].animate.set_color(YELLOW),
        )
        self.wait()

        self.play(
            eq_con[0][6:9].animate.set_color(WHITE),
            eq_con[0][18:22].animate.set_color(WHITE),
        )
        self.wait(2)

        cont_eq_depois = Tex(" C(I_1, I_2)").next_to(eq_lum, RIGHT)
        cont_eq_depois.shift(RIGHT*0.5)
        self.play(
            ReplacementTransform(eq_con, cont_eq_depois)
        )
        self.wait(2)

        cont_estr = Tex(" \\times S(I_1, I_2)",
            isolate=["S(I_1, I_2)"]).next_to(cont_eq_depois, RIGHT)
        cont_estr[1].shift(RIGHT*0.2)
        self.play(Write(cont_estr))
        self.play(cont_estr[1:].animate.set_color(YELLOW))
        self.wait(3)

        eq_estr = Tex("\\frac{\\sigma_{I_1,I_2} + C_3}{\\sigma_{I_1} \\times \\sigma_{I_2} + C_3}")
        eq_estr.set_x(cont_estr[1].get_x()).set_y(cont_estr[1].get_y()).shift(RIGHT*0.6)
        self.play(
            ReplacementTransform(cont_estr[1], eq_estr)
        )
        self.wait(4)

        self.play(
            eq_estr[0][0:6].animate.set_color(YELLOW),
        )
        self.wait()
        self.play(
            eq_estr[0][0:6].animate.set_color(WHITE),
            eq_estr[0][10:13].animate.set_color(YELLOW),
            eq_estr[0][14:17].animate.set_color(YELLOW),
        )
        self.wait()
        self.play(
            eq_estr[0][10:13].animate.set_color(WHITE),
            eq_estr[0][14:17].animate.set_color(WHITE),
        )
        self.wait(6)

        cont_est_depois = Tex(" S(I_1, I_2)").next_to(cont_eq_depois, RIGHT)
        cont_est_depois.shift(RIGHT*0.5)
        self.play(
            ReplacementTransform(eq_estr, cont_est_depois)
        )

        self.wait(6)

        self.play(
            lum_or.animate.set_color(YELLOW)
        )
        self.play(
            lum_or.animate.set_color(WHITE),
            cont_eq_depois.animate.set_color(YELLOW),
        )
        self.wait(1.5)
        self.play(
            cont_eq_depois.animate.set_color(WHITE),
            cont_est_depois.animate.set_color(YELLOW),
        )
        self.wait(2.5)
        self.play(
            cont_est_depois.animate.set_color(WHITE),
        )
        self.wait(6)
        self.play(
            eq[0].animate.set_color(YELLOW)
        )
        self.wait(2)
        self.play(
            eq[0].animate.set_color(WHITE)
        )

        self.play(
            Uncreate(eq[0]), Uncreate(eq[1]), Uncreate(lum_or),
            Uncreate(cont_eq_depois), Uncreate(cont_est_depois),
            Uncreate(cont_eq[0]), Uncreate(cont_estr[0]),
            Uncreate(title)
        )
        self.wait(2)
