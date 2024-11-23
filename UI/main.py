import flet as ft
import time

# def main(page: ft.Page):
#     page.add(ft.SafeArea(ft.Text("Hello")))


def main(page: ft.Page):

    t = ft.Text(value= "Hello!", color="blue")
    page.controls.append(t)
    page.update()

    t = ft.Text()
    s = ft.Text()
    page.add(t)
    page.add(s)
    t.value = 0

    while True:
        for i in range(61):
            if i == 60:
                t.value += 1
            else:
                s.value = i
                page.update()
                time.sleep(0.02)    

ft.app(main)

