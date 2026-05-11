import streamlit as st
from components.auth import Auth
from components.inventory import Inventory
from components.orders import Orders
from components.chatbot import Chatbot

class GroceryStoreApp:
    def __init__(self):
        self.auth = Auth()
        self.inventory = Inventory()
        self.orders = Orders()
        self.chatbot = Chatbot()

    def run(self):
        st.set_page_config(page_title="Grocery Store Application", page_icon="🍎", layout="centered")
        self.setup_session_state()
        self.render_navigation()

    def setup_session_state(self):
        if "page" not in st.session_state:
            st.session_state["page"] = "home"
        if "role" not in st.session_state:
            st.session_state["role"] = None
        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False

    def render_navigation(self):
        with st.sidebar:
            st.title("Navigation")
            if st.button("Home"):
                st.session_state["page"] = "home"
                st.experimental_rerun()

            if st.session_state["logged_in"]:
                if st.session_state["role"] == "user":
                    if st.button("Orders"):
                        st.session_state["page"] = "orders"
                        st.experimental_rerun()
                elif st.session_state["role"] == "employee":
                    if st.button("Inventory"):
                        st.session_state["page"] = "inventory"
                        st.experimental_rerun()

            if st.button("Logout"):
                self.auth.logout()

        self.render_page()

    def render_page(self):
        if st.session_state["page"] == "home":
            self.auth.render_login_register()
        elif st.session_state["page"] == "inventory":
            self.inventory.render_inventory()
        elif st.session_state["page"] == "orders":
            self.orders.render_orders()
        else:
            st.error("Page not found.")

if __name__ == "__main__":
    app = GroceryStoreApp()
    app.run()