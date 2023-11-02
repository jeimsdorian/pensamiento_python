from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado.html')
    fig = figure()

    valores = int(input('¿De cuanto desea que sea la grafica? '))
    
    x_vals = list(range(valores))
    y_vals = []

    for x in x_vals:
        val = int(input(f'valor de {x} '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)