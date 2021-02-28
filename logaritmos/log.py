from manimlib import *

#manimgl log.py Intro -w
class Intro(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def renderNapier(self):
        image = ImageMobject("napier.png")
        image.scale(1.5)
        self.wait(3)

        #imagem do napier
        self.add(image)
        self.play(FadeIn(image))
        self.play(image.animate.scale(0.5).shift(1 * UP).shift(5.5 * LEFT))
        self.wait(2.4)

        return image

    def renderFirstTexts(self, image):
        #texto
        t1 = Text("John Napier (1550-1617)").set_color(WHITE).scale(0.6)
        t1.align_to(image, UP)
        t1.shift(0.2 * DOWN)

        t2 = Text("Matemático, físico e astrônomo que introduziu os logaritmos.").set_color(WHITE).scale(0.4)
        t2.next_to(t1, DOWN)
        t2.shift(1.5 * RIGHT)

        self.add(t1)
        self.play(Write(t1))
        self.add(t2)
        self.play(Write(t2))

        return t1, t2

    def renderHat(self):
        #chapéu
        hat = SVGMobject('wizard_hat.svg')
        hat.shift(2.6 * UP)
        hat.shift(6.1 * LEFT)
        hat[0].set_style(fill_opacity=1,stroke_width=0,stroke_opacity=0,fill_color='#356ec0')
        hat[1].set_style(fill_opacity=1,stroke_width=0,stroke_opacity=0,fill_color='#356ec0')
        hat[2].set_style(fill_opacity=1,stroke_width=0,stroke_opacity=0,fill_color='#295798')
        hat[3].set_style(fill_opacity=1,stroke_width=0,stroke_opacity=0,fill_color='#295798')

        self.play(ShowCreation(hat))
        self.play(hat.animate.rotate(0.5))

        return hat

    def renderAxes(self):
        #plotando o gráfico
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(0, 22, 2),
            # y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(0, 1),
            # The axes will be stretched so as to match the specified
            # height and width
            height=1,
            width=15,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        axes.shift(1.5*DOWN)

        self.add(axes)
        self.play(ShowCreation(axes))

        x_labels = [
            Tex("0"), Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7"),
            Tex("8"), Tex("9"), Tex("10")
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([i * 1.375, 0, 0]), DOWN)
            x_labels[i].shift(6.1 * LEFT)
            x_labels[i].shift(2 * DOWN)
            self.add(x_labels[i])

        return axes, x_labels

    def renderDotAndPowers(self, axes):
        #PONTO VERMELHO E POTÊNCIAS
        dot = Dot(color=YELLOW)
        dot.move_to(axes.c2p(2, 1))
        self.play(GrowFromCenter(dot, scale=0.5))
        scale_logs = 0.9

        dois_elevado_0 = Tex("2^", "0", "=1").scale(scale_logs)
        dois_elevado_0[1].set_color(BLUE)
        dois_elevado_0.next_to(dot, UP)
        self.add(dois_elevado_0)
        self.play(Write(dois_elevado_0))

        self.play(dot.animate.move_to(axes.c2p(6, 1)))
        dois_elevado_1 = Tex("2^", "1", "=2").scale(scale_logs)
        dois_elevado_1[1].set_color(BLUE)
        dois_elevado_1.next_to(dot, UP)
        self.add(dois_elevado_1)
        self.play(Write(dois_elevado_1))

        self.play(dot.animate.move_to(axes.c2p(10, 1)))
        dois_elevado_2 = Tex("2^","2","=4").scale(scale_logs)
        dois_elevado_2[1].set_color(BLUE)
        dois_elevado_2.next_to(dot, UP)
        self.add(dois_elevado_2)
        self.play(Write(dois_elevado_2))

        self.play(dot.animate.move_to(axes.c2p(18, 1)))
        dois_elevado_3 = Tex("2^","3","=8").scale(scale_logs)
        dois_elevado_3.next_to(dot, UP)
        dois_elevado_3[1].set_color(BLUE)
        self.add(dois_elevado_3)
        self.play(Write(dois_elevado_3))

        return dois_elevado_0, dois_elevado_1, dois_elevado_2, dois_elevado_3, dot

    def renderRectangleAndLogs(self, dois_elevado_0, dois_elevado_1, dois_elevado_2, dois_elevado_3):
        box_potencia1 = SurroundingRectangle(dois_elevado_0[1], stroke_opacity=0.5, stroke_width=2, buff = .05)
        box_potencia2 = SurroundingRectangle(dois_elevado_1[1], stroke_opacity=0.5, stroke_width=2, buff = .05)
        box_potencia3 = SurroundingRectangle(dois_elevado_2[1], stroke_opacity=0.5, stroke_width=2, buff = .05)
        box_potencia4 = SurroundingRectangle(dois_elevado_3[1], stroke_opacity=0.5, stroke_width=2, buff = .05)

        self.play(
            ShowCreation(box_potencia1), ShowCreation(box_potencia2),
            ShowCreation(box_potencia3), ShowCreation(box_potencia4)
        )
        self.wait(2)

        scale_logs = 0.9

        primeiro_log = Tex("log_2^1 =").scale(scale_logs)
        primeiro_log.next_to(dois_elevado_0, UP)
        segundo_log = Tex("log_2^2 =").scale(scale_logs)
        segundo_log.next_to(dois_elevado_1, UP)
        terceiro_log = Tex("log_2^4 =").scale(scale_logs)
        terceiro_log.next_to(dois_elevado_2, UP)
        quarto_log = Tex("log_2^8 =").scale(scale_logs)
        quarto_log.next_to(dois_elevado_3, UP)
        self.add(
            primeiro_log, segundo_log, terceiro_log, quarto_log
        )
        self.play(
            Write(primeiro_log), Write(segundo_log),
            Write(terceiro_log), Write(quarto_log)
        )

        primeiro_log_zero = dois_elevado_0[1].copy()
        self.add(primeiro_log_zero)

        segundo_log_um = dois_elevado_1[1].copy()
        self.add(segundo_log_um)

        terceiro_log_dois = dois_elevado_2[1].copy()
        self.add(terceiro_log_dois)

        quarto_log_tres = dois_elevado_3[1].copy()
        self.add(quarto_log_tres)

        self.play(
            primeiro_log_zero.animate.scale(1.6).move_to(primeiro_log).shift(RIGHT*0.85),
            segundo_log_um.animate.scale(1.6).move_to(segundo_log).shift(RIGHT*0.8),
            terceiro_log_dois.animate.scale(1.6).move_to(terceiro_log).shift(RIGHT*0.8),
            quarto_log_tres.animate.scale(1.6).move_to(quarto_log).shift(RIGHT*0.8)
        )

        return box_potencia1, box_potencia2, box_potencia3, box_potencia4, primeiro_log_zero, segundo_log_um, terceiro_log_dois, quarto_log_tres, primeiro_log, segundo_log, terceiro_log, quarto_log

    def construct(self):
        image = self.renderNapier()
        t1, t2 = self.renderFirstTexts(image)
        self.wait(0.5)
        hat = self.renderHat()

        #Texto: LOGARITMOS?
        self.play(Uncreate(t2))
        self.play(Uncreate(hat))
        self.play(FadeOutToPoint(image, [-10, 0, 0]))

        t3 = Text("Logaritmo?").scale(2)
        t3.shift(2.4 * UP)
        self.play(ReplacementTransform(t1, t3))

        self.wait(5)
        axes, x_labels = self.renderAxes()

        dois_elevado_0, dois_elevado_1, dois_elevado_2, dois_elevado_3, dot = self.renderDotAndPowers(axes)
        self.play(Uncreate(dot))

        rectangle_and_logs = self.renderRectangleAndLogs(dois_elevado_0, dois_elevado_1, dois_elevado_2, dois_elevado_3)
        self.wait(4)

        #DELETA PRATICAMENTE TUDO
        self.play(
            Uncreate(dois_elevado_0), Uncreate(dois_elevado_1),
            Uncreate(dois_elevado_2), Uncreate(dois_elevado_3),
            Uncreate(axes), Uncreate(x_labels[0]), Uncreate(x_labels[1]),
            Uncreate(x_labels[2]), Uncreate(x_labels[3]), Uncreate(x_labels[4]),
            Uncreate(x_labels[5]), Uncreate(x_labels[6]), Uncreate(x_labels[7]),
            Uncreate(x_labels[8]), Uncreate(x_labels[9]), Uncreate(x_labels[10]),
            Uncreate(rectangle_and_logs[0]), Uncreate(rectangle_and_logs[1]), Uncreate(rectangle_and_logs[2]),
            Uncreate(rectangle_and_logs[3]), Uncreate(rectangle_and_logs[4]), Uncreate(rectangle_and_logs[5]),
            Uncreate(rectangle_and_logs[6]), Uncreate(rectangle_and_logs[7]), Uncreate(rectangle_and_logs[8]),
            Uncreate(rectangle_and_logs[9]), Uncreate(rectangle_and_logs[10]), Uncreate(rectangle_and_logs[11])
        )

        self.wait(1)
        self.play(Uncreate(t3))

        lines = VGroup(
            Tex("{{2}}^{{3}} = {{8}}").scale(3),
            Tex("log_{{2}}^{{8}} = {{3}}").scale(4))
        lines.arrange(DOWN, buff=1.5)
        lines[0].set_color_by_tex_to_color_map({
            "2": BLUE,
            "3": RED,
            "8": GREEN,
        })
        lines[1].set_color_by_tex_to_color_map({
            "2": GREEN,
            "8": BLUE,
            "3": RED,
        })
        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.play(lines[0].animate.scale(1.5))
        self.wait(5)
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES
            ),
            **play_kw
        )
        self.play(lines.animate.shift(LEFT*2))
        self.wait()

        arrow_base = Arrow(np.array([-2, -2.3, 0]), np.array([0, -3, 0]), buff=0).set_color(BLUE)
        base = Text("Base").set_color(BLUE).scale(0.8)
        base.next_to(arrow_base, RIGHT).shift(0.3 * DOWN)
        self.add(arrow_base, base)

        arrow_logaritmando = Arrow(np.array([-2, -0.6, 0]), np.array([0, 0, 0]), buff=0).set_color(GREEN)
        logaritmando = Text("Logaritmando").set_color(GREEN).scale(0.8)
        logaritmando.next_to(arrow_logaritmando, RIGHT).shift(0.4 * UP)
        self.add(arrow_logaritmando, logaritmando)

        arrow_logaritmo = Arrow(np.array([1.5, -1.5, 0]), np.array([2, -1.5, 0]), buff=0).set_color(RED)
        logaritmo = Text("Logaritmo").set_color(RED).scale(0.8)
        logaritmo.next_to(arrow_logaritmo, RIGHT)
        self.add(arrow_logaritmo, logaritmo)

        self.play(
            FadeIn(arrow_base), FadeIn(base),
            FadeIn(arrow_logaritmando), FadeIn(logaritmando),
            FadeIn(arrow_logaritmo), FadeIn(logaritmo)
        )
        self.wait(6)

        self.play(
            FadeOutToPoint(arrow_base, [0, 0, 0]), FadeOutToPoint(base, [0, 0, 0]),
            FadeOutToPoint(arrow_logaritmando, [0, 0, 0]), FadeOutToPoint(logaritmando, [0, 0, 0]),
            FadeOutToPoint(arrow_logaritmo, [0, 0, 0]), FadeOutToPoint(logaritmo, [0, 0, 0]),
            FadeOutToPoint(lines[0], [0, 0, 0]), FadeOutToPoint(lines[1], [0, 0, 0])
        )


        #grafo logaritmo
        #plotando o gráfico
        axes = Axes(
            x_range=(-30, 30, 1),
            y_range=(-30, 30, 1),
            height=30,
            width=30,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 1,
            }
        )

        self.add(axes)
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.play(self.camera.frame.animate.shift(UR*2).scale(0.75))

        self.wait(4)

        # Axes.get_graph will return the graph of a function
        x_graph = axes.get_graph(
            lambda x: x,
            color=BLUE,
            x_range=[0, 20],
        )
        x_graph_label = axes.get_graph_label(x_graph, "y = x", buff=0.75)
        x_graph_label.scale(0.8)

        x_labels = [
            Tex("1"), Tex("2"), Tex("3"), Tex("4"),
            Tex("5"), Tex("6"), Tex("7"), Tex("8"),
            Tex("9")
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([i * 0.5, 0, 0]), DOWN).scale(0.6).shift(RIGHT*0.5).shift(UP*0.05)
            self.add(x_labels[i])

        y_labels = [
            Tex("1"), Tex("2"), Tex("3"),
            Tex("4"), Tex("5"), Tex("6"), Tex("7"),
            Tex("8"), Tex("9")
        ]
        for i in range(len(y_labels)):
            y_labels[i].next_to(np.array([0, i*0.5, 0]), UP).scale(0.6).shift(LEFT*0.35).shift(UP*0.1)
            self.add(y_labels[i])

        x_labels2 = [
            Tex("10"), Tex("11"), Tex("12"), Tex("13"),
            Tex("14")
        ]
        for i in range(len(x_labels2)):
            x_labels2[i].next_to(np.array([i * 0.5, 0, 0]), DOWN).scale(0.6).shift(RIGHT*5).shift(UP*0.05)
            self.add(x_labels2[i])

        self.play(ShowCreation(x_graph), FadeIn(x_graph_label, RIGHT))
        self.wait(2)

        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(0, x_graph))
        self.play(GrowFromCenter(dot, scale=0.5))

        x_tracker = ValueTracker(0)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), x_graph)
        )

        text_x_update, number_x_update, text_y_update, number_y_update, end_sentence_update = VGroup(Text("(x="), Integer(), Text(",y="), Integer(), Text(")"))
        text_x_update.set_color(RED).scale(0.4)
        text_y_update.set_color(RED).scale(0.4)
        end_sentence_update.set_color(RED).scale(0.4)

        text_x_update.add_updater(lambda x: x.set_x(dot.get_x() + 0.6).set_y(dot.get_y()))

        def update_x_value(self):
            self.set_value(x_tracker.get_value()).set_width(0.18).set_color(RED).set_x(dot.get_x() + 1.1).set_y(dot.get_y())
        number_x_update.add_updater(update_x_value)

        text_y_update.add_updater(lambda x: x.set_x(dot.get_x() + 1.65).set_y(dot.get_y() - 0.05))

        def update_y_value(self):
            self.set_value(x_tracker.get_value()).set_width(0.18).set_color(RED).set_x(dot.get_x() + 2.2).set_y(dot.get_y())
        number_y_update.add_updater(update_y_value)

        end_sentence_update.add_updater(lambda x: x.set_x(dot.get_x() + 2.45).set_y(dot.get_y() - 0.05))

        self.add(dot, text_x_update, text_y_update, end_sentence_update)
        #self.add(number_x_update, number_y_update)
        self.play(x_tracker.animate.set_value(6), run_time=5)
        self.wait(1)

        import math
        log_graph = axes.get_graph(
            lambda x: math.log(x),
            use_smoothing=False,
            color=YELLOW,
            x_range=[0.1, 16]
        )
        log_label = axes.get_graph_label(log_graph, "y = log(x)", buff=0.15)
        log_label.scale(0.8)

        self.play(
            ReplacementTransform(x_graph.copy(), log_graph),
            FadeTransform(x_graph_label.copy(), log_label),
        )
        self.wait()

        dot_log = Dot(color=RED)
        dot_log.move_to(axes.i2gp(1, log_graph))
        self.add(dot_log)
        self.play(GrowFromCenter(dot_log, scale=0.5))

        log_tracker = ValueTracker(1)
        f_always(
            dot_log.move_to,
            lambda: axes.i2gp(log_tracker.get_value(), log_graph)
        )

        text_x_update_log, number_x_update_log, text_y_update_log, number_y_update_log, end_sentence_update_log = VGroup(Text("(x="), Integer(), Text(",y="), Integer(), Text(")"))
        text_x_update_log.set_color(RED).scale(0.4)
        text_y_update_log.set_color(RED).scale(0.4)
        end_sentence_update_log.set_color(RED).scale(0.4)

        text_x_update_log.add_updater(lambda x: x.set_x(dot_log.get_x() + 0.6).set_y(dot_log.get_y() - 0.2))

        def update_x_value_log(self):
            self.set_value(log_tracker.get_value()).set_width(0.18).set_color(RED).set_x(dot_log.get_x() + 1.1).set_y(dot_log.get_y() - 0.2)
        number_x_update_log.add_updater(update_x_value_log)

        text_y_update_log.add_updater(lambda x: x.set_x(dot_log.get_x() + 1.65).set_y(dot_log.get_y() - 0.05 - 0.2))

        def update_y_value_log(self):
            self.set_value(math.log(log_tracker.get_value())).set_width(0.18).set_color(RED).set_x(dot_log.get_x() + 2.2).set_y(dot_log.get_y() - 0.2)
        number_y_update_log.add_updater(update_y_value_log)

        end_sentence_update_log.add_updater(lambda x: x.set_x(dot_log.get_x() + 2.45).set_y(dot_log.get_y() - 0.05 - 0.2))

        self.add(text_x_update_log, text_y_update_log, end_sentence_update_log)
        #self.add(number_x_update_log, number_y_update_log)
        self.play(log_tracker.animate.set_value(9), run_time=6)
        self.wait(6)
        self.play(
            Uncreate(axes), Uncreate(x_graph_label),
            Uncreate(x_graph),
            Uncreate(x_labels[0]), Uncreate(x_labels[1]),
            Uncreate(x_labels[2]), Uncreate(x_labels[3]),
            Uncreate(x_labels[4]), Uncreate(x_labels[5]),
            Uncreate(x_labels[6]), Uncreate(x_labels[7]),
            Uncreate(x_labels[8]),
            Uncreate(y_labels[0]), Uncreate(y_labels[1]),
            Uncreate(y_labels[2]), Uncreate(y_labels[3]),
            Uncreate(y_labels[4]), Uncreate(y_labels[5]),
            Uncreate(y_labels[6]), Uncreate(y_labels[7]),
            Uncreate(y_labels[8]),
            Uncreate(x_labels2[0]), Uncreate(x_labels2[1]),
            Uncreate(x_labels2[2]), Uncreate(x_labels2[3]),
            Uncreate(x_labels2[4]),

            Uncreate(dot), Uncreate(x_tracker),
            Uncreate(text_x_update), Uncreate(text_y_update),
            #FadeOut(number_x_update), Uncreate(number_y_update),
            Uncreate(end_sentence_update), Uncreate(log_graph), Uncreate(log_label),
            Uncreate(dot_log), Uncreate(log_tracker),
            Uncreate(text_x_update_log),
            Uncreate(text_y_update_log), Uncreate(end_sentence_update_log)
        )

class LogRPG(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-30, 30, 1),
            y_range=(-30, 30, 1),
            height=30,
            width=30,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 1,
            }
        )

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.play(self.camera.frame.animate.shift(RIGHT*5).shift(2*UP).scale(1))

        import math
        log_graph = axes.get_graph(
            lambda x: math.log(x),
            use_smoothing=False,
            color=BLUE,
            x_range=[0.1, 30]
        )
        log_label = axes.get_graph_label(log_graph, "y = log(x)", buff=0.15)
        log_label.scale(0.8)

        self.play(
            Write(log_graph)
        )
        self.wait()

        x_labels = [
            Tex("100"), Tex("200"), Tex("300"),
            Tex("400"), Tex("500"), Tex("600"),
            Tex("700"), Tex("800"), Tex("900"),
            Tex("1000"), Tex("1100"), Tex("1200"), Tex("1300"),
            Tex("1400"), Tex("1500"), Tex("1600"),
            Tex("1700"), Tex("1800"), Tex("1900"),
            Tex("2000"), Tex("2100"), Tex("2200"), Tex("2300")
        ]
        for i in range(len(x_labels)):
            if i < 9:
                x_labels[i].next_to(np.array([i * 0.5, 0, 0]), DOWN).scale(0.5).shift(RIGHT*0.5).shift(UP*0.05)
            else:
                x_labels[i].next_to(np.array([i * 0.5, 0, 0]), DOWN).scale(0.4).shift(RIGHT*0.5).shift(UP*0.05)
            self.add(x_labels[i])

        y_labels = [
            Tex("LV25"), Tex("LV50"), Tex("LV75"), Tex("LV100")
        ]
        for i in range(len(y_labels)):
            y_labels[i].next_to(np.array([0, i*0.5, 0]), UP).scale(0.6).shift(LEFT*0.7).shift(UP*0.1)
            self.add(y_labels[i])
        self.wait(0.5)

        label_graph_x = Text("x = Pontos de Experiência (EXP)", size=0.35, stroke_width=0, fill_opacity=1, slant=ITALIC)
        label_graph_x.next_to(x_labels[-1], 3.5*DOWN).shift(LEFT*3)
        self.play(FadeInFromPoint(label_graph_x, (-3, -3, 0)))
        self.wait(3)

        label_graph_y = Text("y = níveis (LV)", size=0.35, stroke_width=0, fill_opacity=1, slant=ITALIC)
        label_graph_y.shift(LEFT*1.6).shift(UP*4).rotate(PI/2)
        self.play(FadeInFromPoint(label_graph_y, (0, 0, 0)))
        self.wait(3)

        dot = Dot(color=RED)
        dot.move_to(axes.c2p(1, 0))
        self.play(FadeIn(dot, scale=0.5))

        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )

        for x in range(1, 24):
            self.play(dot.animate.move_to(axes.c2p(x, math.log(x))))
        self.wait(3)

        self.play(
            Uncreate(axes), Uncreate(log_graph), Uncreate(log_label),
            Uncreate(label_graph_x), Uncreate(label_graph_y),
            Uncreate(dot), Uncreate(h_line), Uncreate(v_line),
            Uncreate(x_labels[0]), Uncreate(x_labels[1]), Uncreate(x_labels[2]),
            Uncreate(x_labels[3]), Uncreate(x_labels[4]), Uncreate(x_labels[5]),
            Uncreate(x_labels[6]), Uncreate(x_labels[7]), Uncreate(x_labels[8]),
            Uncreate(x_labels[9]), Uncreate(x_labels[10]), Uncreate(x_labels[11]),
            Uncreate(x_labels[12]), Uncreate(x_labels[13]), Uncreate(x_labels[14]),
            Uncreate(x_labels[15]), Uncreate(x_labels[16]), Uncreate(x_labels[17]),
            Uncreate(x_labels[18]), Uncreate(x_labels[19]), Uncreate(x_labels[20]),
            Uncreate(x_labels[21]), Uncreate(x_labels[22]),
            Uncreate(y_labels[0]), Uncreate(y_labels[1]), Uncreate(y_labels[2]),
            Uncreate(y_labels[3])
        )

        for y in y_labels:
            self.play(Uncreate(y))

class Part2(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        lines = VGroup(
            Tex("42 \\times 97 =", isolate=["42", "97"]),
            Tex("10^{1,6232} \\times 10^{1,9867} = ", isolate=["10^{1,6232}", "10^{1,9867}"]),
            Tex("10^{(1,6232 + 1,9867)} = 10^{3,61}"),
            Tex("10^{log_{10}(42)} \\times 10^{log_{10}(97)} = ", isolate=["10^{log_{10}(42)}", "10^{log_{10}(97)}"]),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF*1.5)

        scale_text = 2.5

        lines[0].set_color_by_tex_to_color_map({
            "42": BLUE,
            "97": GREEN,
        }).scale(3).shift(0.6*DOWN)
        lines[1].set_color_by_tex_to_color_map({
            "10^{1,6232}": BLUE,
            "10^{1,9867}": GREEN,
        }).scale(scale_text).shift(0.6*DOWN)
        lines[2].set_color_by_tex_to_color_map({
            "10^{(1,6232 + 1,9867)}": TEAL,
            "10^{3,61}": TEAL,
        }).scale(scale_text).shift(0.6*DOWN)
        lines[3].set_color_by_tex_to_color_map({
            "10^{log_{10}(42)}": BLUE,
            "10^{log_{10}(97)}": GREEN
        }).scale(scale_text).shift(0.6*DOWN)

        self.add(lines[0])
        self.wait(4)

        play_kw = {"run_time": 2}

        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                key_map={
                    "42": "10^{1,6232}",
                    "97": "10^{1,9867}",
                }
            ),

            **play_kw
        )
        self.wait(10)

        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2]
            ),
            **play_kw
        )
        self.wait(6)

        line3 = Tex("10^{3,61} = 4074", isolate=["10^{3,61}", "4074"])
        line3.set_color(TEAL).scale(scale_text).next_to(lines[1], 3*DOWN)

        self.play(FadeOut(lines[2]),
            TransformMatchingTex(
                lines[2], line3
            ),
            **play_kw
        )
        self.wait(2)

        box_mult = SurroundingRectangle(lines[0], stroke_opacity=1, stroke_width=4)
        box_result = SurroundingRectangle(line3[2], stroke_opacity=1, stroke_width=4)
        box_361 = SurroundingRectangle(line3[0], stroke_opacity=1, stroke_width=4)

        #self.play(ShowCreation(box_mult))
        #self.wait(2)
        #self.play(ShowCreation(box_result))
        #self.wait(6)

        self.play(ShowCreation(box_361))
        self.wait(6)

        self.play(
            Uncreate(line3), Uncreate(lines[1]), Uncreate(lines[0]),
            Uncreate(box_mult), Uncreate(box_result)
        )

        '''
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[3],
                key_map={
                    "10^{1,6232}": "10^{log_{10}(42)}",
                    "10^{1,9867}": "10^{log_{10}(97)}",
                }
            ),
            **play_kw
        )
        '''
        self.wait(2)
