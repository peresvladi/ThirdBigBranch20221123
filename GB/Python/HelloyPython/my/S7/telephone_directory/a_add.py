def a():
    import n_l_s
    nls = n_l_s.new_line_separator()
    import c_s
    cs = c_s.character_separator()
    f = input('введите фамилию: ') + cs
    i = input('введите имя: ') + cs
    o = input('введите отчество: ') + cs
    t = input('введите телефон: ') + nls
    fiot = f + i + o + t
    return fiot
import w_t_t_d
w_t_t_d.writing_to_the_database(a())