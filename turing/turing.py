from manimlib import *

import numpy as np

class TM(Scene):
    def construct(self):
        start_node = Circle(radius=0.8, color=WHITE).shift(LEFT*4.8).shift(UP)
        start_label = Text("Início").scale(0.4).next_to(start_node, 0)

        a_node = Circle(radius=0.8, color=WHITE).next_to(start_node, RIGHT*5.5)
        a_label = Text("A").scale(1).next_to(a_node, 0)

        arrow_start_a = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(start_node, RIGHT*0.1).scale(0.9).shift(LEFT*0.1)
        curved_arrow_a = CurvedArrow(LEFT, RIGHT, angle=TAU/2+0.6, color=WHITE, stroke_width=8).scale(0.7).next_to(a_node, 0.1*UP).rotate(PI+0.05).shift(DOWN*0.4).shift(LEFT*0.1)

        b_node = Circle(radius=0.8, color=WHITE).next_to(a_node, RIGHT*5.5)
        b_label = Text("B").scale(1).next_to(b_node, 0)

        arrow_a_b = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(a_node, RIGHT*0.1).scale(0.9).shift(LEFT*0.1)

        end_node = Circle(radius=0.8, color=WHITE).next_to(b_node, RIGHT*5.9)
        end_node_ext = Circle(radius=0.9, color=WHITE).next_to(b_node, RIGHT*5.9).shift(LEFT*0.1)
        end_label = Text("Fim").scale(0.5).next_to(end_node, 0)

        arrow_b_end = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(b_node, RIGHT*0.1).scale(0.9).shift(LEFT*0.1)

        memory = VGroup(
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
            Square(side_length=1), Square(side_length=1),
        ).arrange(RIGHT, buff=0.1).shift(DOWN*2)

        data = VGroup(
            Tex("."), Tex("."),
            Tex("."), Tex("."),
            Tex("."), Tex("."),
            Tex("0"), Tex("1"),
            Tex("1"), Tex("1"),
            Tex("0"), Tex("."),
            Tex("."), Tex("."),
        )

        for m in memory:
            self.play(Write(m), run_time=0.2)

        for m, d in zip(memory, data):
            d.set_x(m.get_x())
            d.set_y(m.get_y())
            self.play(Write(d), run_time=0.1)

        label_start_a = Tex("0,x,R", isolate=[','], color=BLUE).scale(0.5).next_to(arrow_start_a, 0.2*UP).shift(LEFT*0.1)
        label_a_a = Tex("1,x,R", isolate=[','], color=BLUE).scale(0.5).next_to(curved_arrow_a, 0.25*UP)
        label_a_b = Tex("0,x,R", isolate=[','], color=BLUE).scale(0.5).next_to(arrow_a_b, 0.2*UP).shift(LEFT*0.1)
        label_b_end = Tex(".,.,R", isolate=[','], color=BLUE).scale(0.5).next_to(arrow_b_end, 0.2*UP).shift(LEFT*0.1)

        self.wait(8.6)

        self.play(data[6].animate.set_color(BLUE))
        self.wait(0.5)
        self.play(
            data[7].animate.set_color(RED),
            data[8].animate.set_color(RED),
            data[9].animate.set_color(RED)
            )
        self.wait(1.1)
        self.play(data[10].animate.set_color(BLUE))
        self.wait(10)

        self.play(data[6].animate.set_color(WHITE))
        self.play(
            data[7].animate.set_color(WHITE),
            data[8].animate.set_color(WHITE),
            data[9].animate.set_color(WHITE)
            )
        self.play(data[10].animate.set_color(WHITE))

        self.wait(19.5)
        self.play(
            memory[0].animate.set_color(YELLOW),
            data[0].animate.set_color(YELLOW), run_time=0.3)
        i = 0
        for m, d in zip(memory, data):
            self.play(
                memory[i].animate.set_color(WHITE),
                data[i].animate.set_color(WHITE), run_time=0.3)
            if i + 1 >= len(memory):
                break
            self.play(
                memory[i + 1].animate.set_color(YELLOW),
                data[i + 1].animate.set_color(YELLOW), run_time=0.3)
            i += 1
        #self.wait(1.5)

        self.play(
            Write(start_node), Write(start_label), Write(a_node),
            Write(a_label), Write(b_node), Write(b_label),
            Write(end_node), Write(end_node_ext), Write(end_label),
            Write(arrow_start_a), Write(arrow_a_b), Write(arrow_b_end),
            Write(curved_arrow_a)
        )

        self.wait(8)

        self.play(start_node.animate.set_color(YELLOW), start_label.animate.set_color(YELLOW))
        self.play(
            a_node.animate.set_color(YELLOW), a_label.animate.set_color(YELLOW),
            start_node.animate.set_color(WHITE), start_label.animate.set_color(WHITE)
        )
        self.play(
            b_node.animate.set_color(YELLOW), b_label.animate.set_color(YELLOW),
            a_node.animate.set_color(WHITE), a_label.animate.set_color(WHITE),
        )
        self.play(
            end_node.animate.set_color(YELLOW), end_node_ext.animate.set_color(YELLOW),
            end_label.animate.set_color(YELLOW),
            b_node.animate.set_color(WHITE), b_label.animate.set_color(WHITE),
        )

        self.play(
            end_node.animate.set_color(WHITE), end_node_ext.animate.set_color(WHITE),
            end_label.animate.set_color(WHITE),
        )

        self.wait(7)

        self.play(
            end_node.animate.set_color(YELLOW), end_node_ext.animate.set_color(YELLOW),
            end_label.animate.set_color(YELLOW),
        )
        self.wait(11)
        self.play(
            end_node.animate.set_color(WHITE), end_node_ext.animate.set_color(WHITE),
            end_label.animate.set_color(WHITE),
        )
        self.wait(6.2)

        self.add(label_start_a, label_a_a, label_a_b, label_b_end)

        self.wait(10)

        self.play(
            start_node.animate.set_color(YELLOW),
            start_label.animate.set_color(YELLOW)
        )
        self.wait(4)

        arrow_head = Arrow(start=LEFT, end=RIGHT*0.4).scale(0.9).rotate(PI/2).next_to(memory[6], DOWN)
        arrow_head.set_color(YELLOW)

        self.play(ShowCreation(arrow_head), memory[6].animate.set_color(YELLOW))
        self.wait(5)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_start_a, color=GOLD))
        )
        self.wait(6.2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_start_a, color=GOLD))
        )
        self.wait(6)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[6], color=GOLD))
        )
        self.wait(2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_start_a[0], color=GOLD))
        )
        self.wait(7)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_start_a[2], color=GOLD))
        )
        self.wait(1.5)

        to_del = []
        to_del.append(label_start_a[2].copy())

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[6], color=GOLD))
        )

        self.play(
            FadeOut(data[6]),
            to_del[-1].animate.next_to(data[6], 0).set_color(WHITE).scale(2)
        )
        self.wait(11)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_start_a[4], color=GOLD))
        )
        self.wait(10.7)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_start_a[4], color=GOLD))
        )
        self.wait(1.5)

        self.play(
            arrow_head.animate.next_to(memory[7], DOWN),
            memory[6].animate.set_color(WHITE),
            memory[7].animate.set_color(YELLOW),
        )
        self.wait(2)
        self.play(
            start_node.animate.set_color(WHITE),
            start_label.animate.set_color(WHITE),
            a_node.animate.set_color(YELLOW),
            a_label.animate.set_color(YELLOW),
        )
        self.wait(7)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_b, color=GOLD))
        )
        self.wait(3)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a, color=GOLD))
        )
        self.wait(3)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[7], color=GOLD))
        )
        self.wait()

        self.wait(5)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[0], color=GOLD))
        )
        self.wait()

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[2], color=GOLD))
        )
        self.wait()

        to_del.append(label_a_a[2].copy())
        self.play(
            FadeOut(data[7]),
            to_del[-1].animate.next_to(data[7], 0).set_color(WHITE).scale(2)
        )
        self.wait()

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[4], color=GOLD))
        )
        self.wait()

        self.play(
            arrow_head.animate.next_to(memory[8], DOWN),
            memory[7].animate.set_color(WHITE),
            memory[8].animate.set_color(YELLOW),
            a_node.animate.set_color(WHITE),
            a_label.animate.set_color(WHITE),
        )
        self.wait(2)
        self.play(
            a_node.animate.set_color(YELLOW),
            a_label.animate.set_color(YELLOW),
        )
        self.wait(1.5)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[8], color=GOLD))
        )
        self.wait(2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[0], color=GOLD))
        )
        self.wait(1.8)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[2], color=GOLD))
        )
        self.wait()

        to_del.append(label_a_a[2].copy())
        self.play(
            FadeOut(data[8]),
            to_del[-1].animate.next_to(data[8], 0).set_color(WHITE).scale(2)
        )
        self.wait(1.2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[4], color=GOLD))
        )
        self.wait()

        self.play(
            arrow_head.animate.next_to(memory[9], DOWN),
            memory[8].animate.set_color(WHITE),
            memory[9].animate.set_color(YELLOW),
            a_node.animate.set_color(WHITE),
            a_label.animate.set_color(WHITE),
        )
        self.wait(0.6)
        self.play(
            a_node.animate.set_color(YELLOW),
            a_label.animate.set_color(YELLOW),
        )
        self.wait()

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[9], color=GOLD))
        )
        self.wait(0.2)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[0], color=GOLD))
        )
        self.wait(0.6)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[2], color=GOLD))
        )
        self.wait(0.4)

        to_del.append(label_a_a[2].copy())

        self.play(
            FadeOut(data[9]),
            to_del[-1].animate.next_to(data[9], 0).set_color(WHITE).scale(2)
        )
        self.wait()

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_a[4], color=GOLD))
        )
        self.wait(0.2)

        self.play(
            arrow_head.animate.next_to(memory[10], DOWN),
            memory[9].animate.set_color(WHITE),
            memory[10].animate.set_color(YELLOW),
            a_node.animate.set_color(WHITE),
            a_label.animate.set_color(WHITE),
        )
        self.wait()
        self.play(
            a_node.animate.set_color(YELLOW),
            a_label.animate.set_color(YELLOW),
        )
        self.wait(3)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[10], color=GOLD))
        )
        self.wait(3.6)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_b[0], color=GOLD))
        )
        self.wait()

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_b[2], color=GOLD))
        )
        self.wait()

        to_del.append(label_a_b[2].copy())

        self.play(
            FadeOut(data[10]),
            to_del[-1].animate.next_to(data[10], 0).set_color(WHITE).scale(2)
        )
        self.wait(1.5)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_a_b[4], color=GOLD))
        )
        self.wait(0.4)

        self.play(
            arrow_head.animate.next_to(memory[11], DOWN),
            memory[10].animate.set_color(WHITE),
            memory[11].animate.set_color(YELLOW),
        )
        self.wait()
        self.play(
            a_node.animate.set_color(WHITE),
            a_label.animate.set_color(WHITE),
        )
        self.play(
            b_node.animate.set_color(YELLOW),
            b_label.animate.set_color(YELLOW),
        )
        self.wait(0.8)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_b_end, color=GOLD))
        )
        self.wait(0.6)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(data[11], color=GOLD))
        )

        self.wait(7.5)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_b_end[0], color=GOLD))
        )
        self.wait(0.4)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_b_end[2], color=GOLD))
        )
        self.wait()

        to_del.append(label_b_end[2].copy())
        self.play(
            FadeOut(data[11]),
            to_del[-1].animate.next_to(data[11], 0).set_color(WHITE).scale(2)
        )
        self.wait(0.7)

        self.play(
            ShowCreationThenDestruction(SurroundingRectangle(label_b_end[4], color=GOLD))
        )
        self.wait(0.4)

        self.play(
            arrow_head.animate.next_to(memory[12], DOWN),
            memory[11].animate.set_color(WHITE),
            memory[12].animate.set_color(YELLOW),
            b_node.animate.set_color(WHITE),
            b_label.animate.set_color(WHITE),
        )
        self.wait(0.5)
        self.play(
            end_node.animate.set_color(YELLOW),
            end_node_ext.animate.set_color(YELLOW),
            end_label.animate.set_color(YELLOW),
        )
        self.wait(17)

        self.play(
            Uncreate(start_node), Uncreate(start_label), Uncreate(a_node), Uncreate(a_label),
            Uncreate(arrow_start_a), Uncreate(curved_arrow_a), Uncreate(b_node), Uncreate(b_label),
            Uncreate(arrow_a_b), Uncreate(end_node), Uncreate(end_node_ext), Uncreate(end_label),
            Uncreate(arrow_b_end), Uncreate(memory), Uncreate(label_start_a),
            Uncreate(label_a_a), Uncreate(label_a_b), Uncreate(label_b_end), Uncreate(arrow_head),
            Uncreate(to_del[0]), Uncreate(to_del[1]), Uncreate(to_del[2]),
            Uncreate(to_del[3]), Uncreate(to_del[4]), Uncreate(to_del[5]),
            Uncreate(data[0]), Uncreate(data[1]), Uncreate(data[2]),
            Uncreate(data[3]), Uncreate(data[4]), Uncreate(data[12]), Uncreate(data[5]),
        )
        self.wait(3)

class LabelMT(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Máquina de", stroke_width=3, stroke_color=BLACK).scale(1.75)
        ord2 = Text("Turing", stroke_width=3, stroke_color=BLACK).scale(1.75)
        g = VGroup(ord, ord2).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class LabelAno(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("1936", stroke_width=3, stroke_color=BLACK).scale(1.75)
        #ord2 = Text("Turing", stroke_width=3, stroke_color=BLACK).scale(1.75)
        g = VGroup(ord).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class DavidHilbert(Scene):
    def construct(self):
        image = ImageMobject("hilbert.png")

        #imagem do hilbert
        self.add(image)
        self.play(FadeIn(image))
        self.play(image.animate.scale(0.5).shift(2 * UP).shift(5.7 * LEFT))
        self.wait(0.4)

        #texto
        t1 = Text("David Hilbert (1862-1943)").set_color(WHITE).scale(0.6).shift(0.3*LEFT)
        t1.align_to(image, UP)

        t2 = Text("Matemático alemão dos mais influentes de seu tempo.").set_color(WHITE).scale(0.37)
        t2.next_to(t1, DOWN)
        t2.shift(RIGHT*1.1)

        self.add(t1)
        self.play(Write(t1))
        self.add(t2)
        self.play(Write(t2))

        self.wait(1)

        #imagem do hilbert
        math_image = ImageMobject("math.png")
        math_image.shift(DOWN*1.4)
        self.add(math_image)
        self.play(FadeIn(math_image))
        self.wait(0.5)

        self.play(
            FadeOut(image), Uncreate(t1), Uncreate(t2), FadeOut(math_image)
        )

        self.wait()

class Axioma(Scene):
    def construct(self):
        '''
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)
        '''

        ord = Text("Axiomas são definições básicas por si só,", stroke_color=BLACK).scale(0.6)
        ord2 = Text("de maneira que são óbvias e não demandam", stroke_color=BLACK).scale(0.6)
        ord3 = Text("demonstração.", stroke_color=BLACK).scale(0.6)

        g = VGroup(ord, ord2, ord3).arrange(DOWN)

        self.play(Write(g))
        self.wait(4)

        a_ord = Text("Um exemplo simples de axioma é, por exemplo,", stroke_color=BLACK).scale(0.55)
        a_ord2 = Text("afirmar que \"a menor distância entre 2 pontos", stroke_color=BLACK).scale(0.55)
        a_ord3 = Text("é o segmento de reta que liga estes pontos\".", stroke_color=BLACK).scale(0.55)

        g2 = VGroup(a_ord, a_ord2, a_ord3).arrange(DOWN)

        self.play(ReplacementTransform(g, g2))
        self.wait(7)

        self.play(Uncreate(g2))
        self.wait(2)

class LabelProgramaHilbert(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Programa de", stroke_width=3, stroke_color=BLACK).scale(1.75)
        ord2 = Text("Hilbert", stroke_width=3, stroke_color=BLACK).scale(1.75)
        g = VGroup(ord, ord2).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class Propriedade1(Scene):
    def construct(self):
        '''
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)
        '''

        title = Text("1º enunciado:", color=GOLD).scale(0.7).to_edge(UP).shift(DOWN)
        ord2 = Text("A matemática deve ser descrita usando", stroke_color=BLACK).scale(0.66)
        ord3 = Text("sempre os mesmos símbolos e a mesma", stroke_color=BLACK).scale(0.66)
        ord4 = Text("linguagem.", stroke_color=BLACK).scale(0.66)

        g = VGroup(ord2, ord3, ord4).arrange(DOWN*1.5).shift(0.5*DOWN)
        ord4.shift(0.1*UP)

        self.play(Write(title), Write(g))
        self.wait(4)

        self.play(Uncreate(title), Uncreate(g))

class Propriedade2(Scene):
    def construct(self):
        '''
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)
        '''

        title = Text("2º enunciado (Completude):", color=GOLD).scale(0.8).to_edge(UP).shift(DOWN)
        ord2 = Text("Toda afirmação matemática deve", stroke_color=BLACK).scale(0.75)
        ord3 = Text("ser demonstrada nesse sistema.", stroke_color=BLACK).scale(0.75)
        #ord4 = Text("linguagem.", stroke_color=BLACK).scale(0.66)

        g = VGroup(ord2, ord3).arrange(DOWN*1.5).shift(0.5*DOWN)
        #ord4.shift(0.1*UP)

        self.play(Write(title), Write(g))
        self.wait(6)

        self.play(Uncreate(title), Uncreate(g))

class Propriedade3(Scene):
    def construct(self):
        '''
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)
        '''

        title = Text("3º enunciado (Consistência):", color=GOLD).scale(0.8).to_edge(UP).shift(DOWN)
        ord2 = Text("Nenhuma inconsistência pode", stroke_color=BLACK).scale(0.75)
        ord3 = Text("ser obtida nesse sistema.", stroke_color=BLACK).scale(0.75)
        #ord4 = Text("linguagem.", stroke_color=BLACK).scale(0.66)

        g = VGroup(ord2, ord3).arrange(DOWN*1.5).shift(0.5*DOWN)
        #ord4.shift(0.1*UP)

        self.play(Write(title), Write(g))
        self.wait(6)

        self.play(Uncreate(title), Uncreate(g))

class Propriedade4(Scene):
    def construct(self):
        '''
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)
        '''

        title = Text("4º enunciado (Decidibilidade):", color=GOLD).scale(0.7).to_edge(UP).shift(DOWN)
        ord2 = Text("Deve existir algum procedimento", stroke_color=BLACK).scale(0.62)
        ord3 = Text("capaz de verificar (decidir) se", stroke_color=BLACK).scale(0.62)
        ord4 = Text("uma proposição matemática é verdadeira", stroke_color=BLACK).scale(0.62)
        ord5 = Text("ou falsa nesse sistema.", stroke_color=BLACK).scale(0.62)

        g = VGroup(ord2, ord3, ord4, ord5).arrange(DOWN*1.5).shift(0.5*DOWN)
        #ord4.shift(0.1*UP)

        self.play(Write(title), Write(g))
        self.wait(7)

        self.play(Uncreate(title), Uncreate(g))

class Resumo(Scene):
    def construct(self):
        '''
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)
        '''

        title = Text("Resumo do Programa de Hilbert:", color=GOLD).scale(0.75).to_edge(UP).shift(DOWN)
        ord2 = Text("1. Mesma linguagem e mesmos símbolos.", stroke_color=BLACK).scale(0.65)
        ord3 = Text("2. Completude.", stroke_color=BLACK).scale(0.7)
        ord4 = Text("3. Consistência.", stroke_color=BLACK).scale(0.7)
        ord5 = Text("4. Decidibilidade.", stroke_color=BLACK).scale(0.7)

        g = VGroup(ord2, ord3, ord4, ord5).arrange(DOWN*1.5).shift(0.5*DOWN)
        ord4.shift(0.1*UP)
        ord5.shift(0.1*UP)

        self.play(Write(title), Write(g))
        self.wait(5)

        self.play(Uncreate(title), Uncreate(g))

class KurtGodel(Scene):
    def construct(self):
        image = ImageMobject("godel.png")

        #imagem do godel
        self.add(image)
        self.play(FadeIn(image))
        self.play(image.animate.scale(0.5).shift(1.9*UP).shift(5.7 * LEFT))
        self.wait(0.4)

        #texto
        t1 = Text("Kurt Gödel (1906-1978)").set_color(WHITE).scale(0.6).shift(0.7*LEFT)
        t1.align_to(image, UP)

        t2 = Text("Matemático austríaco, considerado um dos lógicos mais importantes dos séculos 19 e 20.").set_color(WHITE).scale(0.37)
        t2.next_to(t1, DOWN)
        t2.shift(RIGHT*1.79)

        t3 = Text("Foi responsável pelos Teoremas da Incompletude, que mostraram não ser possível existir Completude no Programa de Hilbert.").set_color(WHITE).scale(0.37)
        t3.next_to(t2, DOWN)
        t3.shift(LEFT*0.22)

        self.add(t1)
        self.play(Write(t1))
        self.add(t2)
        self.play(Write(t2))
        self.add(t2)
        self.play(Write(t3))

        self.wait()

        godel_einstein = ImageMobject("godel_einstein.png")

        #imagem do godel
        self.add(godel_einstein)
        godel_einstein.scale(0.8).set_x(-10).set_y(-2.2)
        self.play(godel_einstein.animate.shift(7 * RIGHT))

        label_foto = Text("Godel e Einstein eram parças!", color=GOLD).scale(0.4)
        self.add(label_foto)
        label_foto.set_x(10).set_y(-2.2)
        self.play(label_foto.animate.shift(7 * LEFT))

        self.wait(2)

        self.play(
            FadeOut(image), Uncreate(t1), Uncreate(t2), Uncreate(t3), FadeOut(godel_einstein),
            Uncreate(label_foto)
        )

        self.wait()

class LabelSentenca(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("\"Essa sentença não", stroke_width=3, stroke_color=BLACK).scale(1.2)
        ord2 = Text("pode ser provada\".", stroke_width=3, stroke_color=BLACK).scale(1.2)
        g = VGroup(ord, ord2).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class LabelDecidibilidade(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Decidibilidade", stroke_width=3, stroke_color=BLACK).scale(1.75)
        g = VGroup(ord).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class LabelPP(Scene):
    def construct(self):
        background = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT,
        stroke_width = 0,
        fill_color = "#009933",
        fill_opacity = 1)
        self.add(background)

        ord = Text("Problema da", stroke_width=3, stroke_color=BLACK).scale(1.75)
        ord2 = Text("Parada", stroke_width=3, stroke_color=BLACK).scale(1.75)
        g = VGroup(ord, ord2).arrange(DOWN)

        self.play(Write(g))
        self.wait(5)

        self.play(Uncreate(g))
        self.wait(2)

class AlgExample(Scene):
    def construct(self):
        title = Text("Algoritmo que acha o maior valor entre 3 números", color=GOLD).scale(0.5).to_edge(UP)
        self.play(Write(title))

        border = RoundedRectangle(corner_radius=1, height=6.5, width=8).shift(0.4*DOWN)
        self.play(ShowCreation(border))
        #input_label = Tex("Valores de entrada: (a, b, c)").next_to(title)

        #if a > 1:
        #    print("bla")

        line1 = Text("Valores de Entrada: (a, b, c)").scale(0.4).set_x(border.get_x()).set_y(border.get_y() + 2.75)
        line1[20].set_color(WHITE)
        line1[21].set_color(BLUE)
        line1[24].set_color(BLUE)
        line1[27].set_color(BLUE)
        line1[28].set_color(WHITE)
        line2 = Text("Se a for maior do que b:").scale(0.4)
        line2.next_to(line1, direction=DOWN, aligned_edge=LEFT)
        line2[0:2].set_color(PURPLE)
        line2[3:-2].set_color(PURPLE)
        line2[3].set_color(BLUE)
        line2[-2].set_color(BLUE)
        Trac2 = DashedLine(UP, DOWN*1.4, dash_length=0.1).next_to(line2, direction=DOWN, aligned_edge=LEFT).shift(UP*0.2)
        line3 = Text("Se a for maior do que c:").scale(0.4).shift(UP*0.1)
        line3.next_to(line2, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line3[0:2].set_color(PURPLE)
        line3[3:-2].set_color(PURPLE)
        line3[3].set_color(BLUE)
        line3[-2].set_color(BLUE)
        Trac1 = DashedLine(UP, DOWN*0.1, dash_length=0.1).scale(0.7).next_to(line3, direction=DOWN, aligned_edge=LEFT).shift(UP*0.25)
        line4 = Text("Então a é o maior número.").scale(0.4)
        line4.next_to(line3, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line4.set_color(PURPLE)
        line4[6].set_color(BLUE)
        line4[12:17].set_color(RED)
        line5 = Text("Caso contrário:").scale(0.4)
        line5.next_to(line4, direction=DOWN, aligned_edge=LEFT).shift(LEFT*0.5)
        line5[:-1].set_color(PURPLE)
        line6 = Text("c é o maior número.").scale(0.4)
        line6.next_to(line5, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line6.set_color(PURPLE)
        line6[0].set_color(BLUE)
        line6[6:11].set_color(RED)
        line7 = Text("Caso contrário:").scale(0.4)
        line7.next_to(line6, direction=DOWN, aligned_edge=LEFT).shift(LEFT)
        line7[:-1].set_color(PURPLE)
        line8 = Text("Se b for maior do que c:").scale(0.4)
        line8.next_to(line7, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line8[0:2].set_color(PURPLE)
        line8[3:-2].set_color(PURPLE)
        line8[3].set_color(BLUE)
        line8[-2].set_color(BLUE)
        Trac3 = DashedLine(UP, DOWN*0.1, dash_length=0.1).scale(0.7).next_to(line8, direction=DOWN, aligned_edge=LEFT).shift(UP*0.25)
        line9 = Text("Então b é o maior número.").scale(0.4)
        line9.set_color(PURPLE)
        line9[6].set_color(BLUE)
        line9[12:17].set_color(RED)
        line9.next_to(line8, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line10 = Text("Caso contrário:").scale(0.4)
        line10.next_to(line9, direction=DOWN, aligned_edge=LEFT).shift(LEFT*0.5)
        line10[:-1].set_color(PURPLE)
        line11 = Text("c é o maior número.").scale(0.4)
        line11.next_to(line10, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line11.set_color(PURPLE)
        line11[0].set_color(BLUE)
        line11[6:11].set_color(RED)

        g = VGroup(
            line1, line2, line3, line4, line5, line6, line7, line8,
            line9, line10, line11
        )

        self.play(
            Write(g), ShowCreation(Trac1), ShowCreation(Trac2),
            ShowCreation(Trac3)
        )

        self.wait(4)

        i1 = Text("a = 3").scale(0.5).next_to(border, LEFT).shift(UP).shift(LEFT*0.6)
        i1[0].set_color(BLUE)
        ti1 = Text("Entrada", color=GOLD).scale(0.5).next_to(i1, UP)
        i2 = Text("b = 8").scale(0.5).next_to(i1, DOWN)
        i2[0].set_color(BLUE)
        i3 = Text("c = 5").scale(0.5).next_to(i2, DOWN)
        i3[0].set_color(BLUE)
        a = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(i3, DOWN)

        self.play(Write(i1), Write(i2), Write(i3), Write(a), Write(ti1))
        self.wait(4)

        o1 = Text("Maior = 8").scale(0.5).next_to(border, RIGHT).shift(0.6*UP)
        o1[0:5].set_color(RED)
        to1 = Text("Saída", color=GOLD).scale(0.5).next_to(o1, UP)
        ao = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(o1, DOWN)

        self.play(Write(o1), Write(ao), Write(to1))

        self.wait(4)
        self.play(
            Uncreate(title), Uncreate(border), Uncreate(g), Uncreate(Trac1),
            Uncreate(Trac2), Uncreate(Trac3), Uncreate(o1), Uncreate(ao), Uncreate(to1),
            Uncreate(i1), Uncreate(i2), Uncreate(i3), Uncreate(a), Uncreate(ti1)
        )
        self.wait()

class AlgParada(Scene):
    def construct(self):
        title = Text("Algoritmo que verifica se outro algoritmo \"termina\"", color=GOLD).scale(0.45).to_edge(UP)
        self.play(Write(title))

        border = RoundedRectangle(corner_radius=1, height=6.5, width=8).shift(0.4*DOWN)
        self.play(ShowCreation(border))
        #input_label = Tex("Valores de entrada: (a, b, c)").next_to(title)

        #if a > 1:
        #    print("bla")

        line1 = Text("Valores de Entrada: (A, a)").scale(0.4).set_x(border.get_x()).set_y(border.get_y() + 2.75)
        line1[20].set_color(WHITE)
        line1[21].set_color(BLUE)
        line1[22].set_color(BLUE)
        line1[24].set_color(BLUE)
        line1[25].set_color(WHITE)
        line2 = Text("?").scale(6)
        line2.next_to(line1, direction=DOWN, aligned_edge=LEFT)
        line2.shift(RIGHT*2.2).shift(DOWN*0.5)
        '''
        line2[0:2].set_color(PURPLE)
        line2[3:-2].set_color(PURPLE)
        line2[3].set_color(BLUE)
        line2[-2].set_color(BLUE)
        Trac2 = DashedLine(UP, DOWN*1.4, dash_length=0.1).next_to(line2, direction=DOWN, aligned_edge=LEFT).shift(UP*0.2)
        line3 = Text("Se a for maior do que c:").scale(0.4).shift(UP*0.1)
        line3.next_to(line2, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line3[0:2].set_color(PURPLE)
        line3[3:-2].set_color(PURPLE)
        line3[3].set_color(BLUE)
        line3[-2].set_color(BLUE)
        Trac1 = DashedLine(UP, DOWN*0.1, dash_length=0.1).scale(0.7).next_to(line3, direction=DOWN, aligned_edge=LEFT).shift(UP*0.25)
        line4 = Text("Então a é o maior número.").scale(0.4)
        line4.next_to(line3, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line4.set_color(PURPLE)
        line4[6].set_color(BLUE)
        line4[12:17].set_color(RED)
        line5 = Text("Caso contrário:").scale(0.4)
        line5.next_to(line4, direction=DOWN, aligned_edge=LEFT).shift(LEFT*0.5)
        line5[:-1].set_color(PURPLE)
        line6 = Text("c é o maior número.").scale(0.4)
        line6.next_to(line5, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line6.set_color(PURPLE)
        line6[0].set_color(BLUE)
        line6[6:11].set_color(RED)
        line7 = Text("Caso contrário:").scale(0.4)
        line7.next_to(line6, direction=DOWN, aligned_edge=LEFT).shift(LEFT)
        line7[:-1].set_color(PURPLE)
        line8 = Text("Se b for maior do que c:").scale(0.4)
        line8.next_to(line7, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line8[0:2].set_color(PURPLE)
        line8[3:-2].set_color(PURPLE)
        line8[3].set_color(BLUE)
        line8[-2].set_color(BLUE)
        Trac3 = DashedLine(UP, DOWN*0.1, dash_length=0.1).scale(0.7).next_to(line8, direction=DOWN, aligned_edge=LEFT).shift(UP*0.25)
        line9 = Text("Então b é o maior número.").scale(0.4)
        line9.set_color(PURPLE)
        line9[6].set_color(BLUE)
        line9[12:17].set_color(RED)
        line9.next_to(line8, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line10 = Text("Caso contrário:").scale(0.4)
        line10.next_to(line9, direction=DOWN, aligned_edge=LEFT).shift(LEFT*0.5)
        line10[:-1].set_color(PURPLE)
        line11 = Text("c é o maior número.").scale(0.4)
        line11.next_to(line10, direction=DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        line11.set_color(PURPLE)
        line11[0].set_color(BLUE)
        line11[6:11].set_color(RED)
        '''

        g = VGroup(
            line1, line2
        )

        self.play(
            Write(g)
        )

        i1 = Text("Algoritmo A").scale(0.4).next_to(border, LEFT).shift(UP).shift(0.2*LEFT)
        i1.set_color(BLUE)
        ti1 = Text("Entrada", color=GOLD).scale(0.5).next_to(i1, UP)
        i2 = Text("Entrada a").scale(0.4).next_to(i1, DOWN)
        i2.set_color(BLUE)
        '''
        i3 = Text("c = 5").scale(0.5).next_to(i2, DOWN)
        i3[0].set_color(BLUE)
        '''
        a = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(i2, DOWN)

        self.play(Write(i1), Write(i2), Write(a), Write(ti1))

        o1 = Text("Sim / Não ?").scale(0.4).next_to(border, RIGHT).shift(0.6*UP).shift(0.2*RIGHT)
        o1.set_color(RED)
        to1 = Text("Saída", color=GOLD).scale(0.5).next_to(o1, UP)
        ao = Arrow(start=LEFT, end=RIGHT, color=WHITE).next_to(o1, DOWN)

        self.play(Write(o1), Write(ao), Write(to1))

        self.wait(4)
        self.play(
            Uncreate(title), Uncreate(border), Uncreate(g),
            Uncreate(o1), Uncreate(ao), Uncreate(to1),
            Uncreate(i1), Uncreate(i2), Uncreate(a), Uncreate(ti1)
        )
        self.wait()
