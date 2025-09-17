from flet import *

def main(page: Page):
    page.title="Rakwan"
    page.window.height = 740
    page.window.width = 390
    page.window.top = 10
    page.window.left=960
    page.theme_mode = ThemeMode.LIGHT

    def route_change(r): 
        page.views.clear()
        ############ index page ##########
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title=Text("Rakwan python"),
                        color='white',
                        bgcolor=colors.PURPLE #purple
                        ),
                    
                    Text("\n\n\n\nWelcome ...",size=24,color='black',width=370,text_align='center'),
                    
                    Row([Image(src="login.gif",width=280)],alignment=MainAxisAlignment.CENTER),
                    Text("اهلاو سهلا بك في تطبيقنا",size=16,color='purple',width=370,text_align='center'),
                    Row([
                        ElevatedButton(
                        "دخول للحساب",
                        width=170,
                        style=ButtonStyle(bgcolor='purple',color='white',padding=15,shape=ContinuousRectangleBorder(radius=5)),
                        on_click=lambda _: page.go("/login")
                        ),
                    ElevatedButton(
                        "انشأ حساب",
                        width=170,
                        style=ButtonStyle(bgcolor='purple',color='white',padding=15,shape=ContinuousRectangleBorder(radius=5)),
                        on_click=lambda _: page.go("/signup")
                        ),
                    ],alignment=MainAxisAlignment.CENTER)
                ],
            )
        )
        ########### login page ############
        if page.route == "/login":
            page.views.append(
                View(
                    "/login",
                    [
                        AppBar(title=Text("Login system"),color='white', bgcolor=colors.PURPLE),
                        Text("\n تسجيل الدخول للحساب \n",size=21,color='purple',width=370,text_align='center'),
                        TextField(label='Email(البريد الالكتروني)'),
                        TextField(label='Password(كلمة المرور)',password=True,can_reveal_password=True),
                        CupertinoCheckbox(label="Remember me ! تذكرني", value=True),
                        Row([
                        ElevatedButton(
                        "دخول الان",
                        width=170,
                        style=ButtonStyle(bgcolor='purple',color='white',padding=15,shape=ContinuousRectangleBorder(radius=5)),
                        
                        on_click=lambda _: page.go("/login")
                                ),
                    ElevatedButton(
                        "انشأ حساب",
                        width=170,
                        style=ButtonStyle(bgcolor='purple',color='white',padding=15,shape=ContinuousRectangleBorder(radius=5)),
                        on_click=lambda _: page.go("/signup")
                        ),
                    ],alignment=MainAxisAlignment.CENTER)
                    ],
                ),
            )
         
        ########### signup page ############    
        if page.route == "/signup":
            page.views.append(
                View(
                    "/signup",
                    [
                        AppBar(title=Text("Sign up"),color='white', bgcolor=colors.PURPLE),
                        Text("\n انشاء حساب جديد \n",size=21,color='purple',width=370,text_align='center'),
                        Row([
                            TextField(label='First name',width=170),
                            TextField(label='Last name',width=170),
                            ]),
                        TextField(label='Email'),
                        
                        Row([
                            TextField(label='password',width=170),
                        TextField(label='repeat password',width=170),
                            ]),
                        
                    Row([
                        ElevatedButton(
                        "انشاء الان",
                        width=170,
                        style=ButtonStyle(bgcolor='purple',color='white',padding=15,shape=ContinuousRectangleBorder(radius=5)),
                        on_click=lambda _: page.go("/login")
                        ),
                        ElevatedButton(
                        "ليدك حساب !",
                        width=170,
                        style=ButtonStyle(bgcolor='purple',color='white',padding=15,shape=ContinuousRectangleBorder(radius=5)),
                        on_click=lambda _: page.go("/login")
                        ),
                    ],alignment=MainAxisAlignment.CENTER)
                        
                    ],
                ),
            )
        
        page.update()
    ###########################################
    def go_page(e):
        page.views.pop()
        back_page = page.views[-1]
        page.go(back_page.route)

    page.on_route_change = route_change
    page.on_view_pop = go_page
    page.go(page.route)


app(target=main)
