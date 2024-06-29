import reflex as rx




class SignUp(rx.State):
    
    form_data = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        form_data["username"]=self.form_data["username"]
        form_data["pharmacy"]=self.form_data["pharmacy"]
        form_data["incoporation_no"]=self.form_data["incoporation_no"]
        form_data["liscence"]=self.form_data["liscence"]
        print(form_data)
        
    def commit(self, form_data: dict):
        self.form_data = form_data

