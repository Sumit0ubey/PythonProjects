#  RMS - Resturant Mangement System 

class RMS:
    def __init__(self, restaurant_name, restaurant_menu):
        self.rest_name = restaurant_name
        self.user_order = ''
        self.menu = restaurant_menu
        self.total_bill = 0

    def welcome_user(self):
        # Welcome user
        print('Welcome to the', self.rest_name.title())

    def take_order(self):
        # Take order
        self.user_order = input('Please place your order here:')

    def display_menu(self):
        # Display menu
        print('Menu:')
        print("*" * 30)
        for i in self.menu:
            print(i.title(), self.menu[i])
        print("*" * 30)

    def preparing_order(self):
        # Preparing order
        import time
        print('Preparing your', self.user_order.title())
        time.sleep(1)
        self.total_bill = self.total_bill + self.menu[self.user_order.lower()]

    def serve_order(self):
        # Serve order
        print('Your order is ready!')

    def display_bill(self):
        # Display bill
        print('Your bill:', self.total_bill)

    def verify_bill(self):
        self.user_pay = int(input('Please pay your bill here:'))
        # Verify bill
        while self.user_pay < self.total_bill:
            self.total_bill = self.total_bill - self.user_pay
            print('Payment Failed! Please pay more', self.total_bill)
            self.user_pay = int(input('Please pay your bill here:'))
        if self.user_pay > self.total_bill:
            print('Here is your change', self.user_pay - self.total_bill)
        else:
            pass

    def ty(self):
        # Thank you
        print('Thank you for visiting', self.rest_name.title())

    def order_process(self):
        self.welcome_user()
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.ask_user = input('Do you want to order again?')
            while self.ask_user.lower() == 'yes':
                self.repeat_order()
                self.ask_user = input('Do you want to order again?')
            self.display_bill()
            self.verify_bill()
            self.ty()
        else:
            print('Invalid Order!')
            self.order_process()

    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
        else:
            print('Invalid order')
            self.repeat_order()

if __name__ == '__main__':
    menu = {'Ramen': 250, 'Oden': 200, 'Sushi': 400, 'Samosa Ramen': 450, 'Custom dis': 600}
    mc = RMS(restaurant_name='Indo-Japan Point', restaurant_menu=menu)
    mc.order_process()
