import flet as ft


def main(page: ft.Page):
    page.title = "WebView Browser"
    page.padding = 0

    # 1. เก็บ URL ปัจจุบันไว้ในตัวแปร
    state = {"url": "https://www.wikipedia.org"}

    # 2. ฟังก์ชันสร้าง WebView (แยกออกมาให้เรียกใช้ง่าย)
    def get_new_webview():
        try:
            return ft.WebView(
                url=state["url"],
                expand=True,
                on_page_started=lambda _: print("Loading..."),
                on_page_ended=lambda _: print("Loaded!")
            )
        except:
            return ft.Text(f"Web: {state['url']}")

    # 3. ฟังก์ชันบันทึกและ "บังคับรีโหลด"
    def save_url(e):
        if url_input.value:
            new_url = url_input.value
            if not new_url.startswith("http"):
                new_url = "https://" + new_url

            # อัปเดตค่า URL ใน state
            state["url"] = new_url

            # --- เทคนิคขั้นเด็ดขาดสำหรับ Android ---
            # ลบทุกอย่างในหน้าจอออกให้เกลี้ยง
            page.controls.clear()
            page.update()

            # ใส่ WebView ตัวใหม่ที่สร้างจาก URL ใหม่เข้าไป
            page.add(get_new_webview())

            dialog.open = False
            page.update()

    # 4. ส่วนประกอบ UI (Dialog และ AppBar)
    url_input = ft.TextField(label="ระบุ URL", value=state["url"])
    dialog = ft.AlertDialog(
        title=ft.Text("เปลี่ยนเว็บไซต์"),
        content=url_input,
        actions=[ft.TextButton(content=ft.Text("บันทึก"), on_click=save_url)],
    )
    page.overlay.append(dialog)

    page.appbar = ft.AppBar(
        title=ft.Text("Application"),
        actions=[
            ft.Container(
                content=ft.Text("☰", size=25),
                on_click=lambda _: setattr(dialog, "open", True) or page.update(),
                padding=10
            )
        ],
    )

    # เริ่มต้นครั้งแรก
    page.add(get_new_webview())


if __name__ == "__main__":
    ft.app(main)