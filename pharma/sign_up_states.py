import reflex as rx




class SignUp(rx.State):
    
    form_data = {}

    def handle_submit(self, user_input: dict):
        self.form_data["username"] = user_input["username"]
        self.form_data["pharmacy"] = user_input["pharmacy"]
        self.form_data["incoporation_no"] = user_input["incoporation_no"]
        self.form_data["liscence"] = user_input["liscence"]
        
        
    def commit(self):
        print(self.form_data)