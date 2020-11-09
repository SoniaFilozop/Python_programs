class MailClient:
    def __init__(self, server, user):
        self.servers = {}
        self.server = server
        self.user = user

    def add_user_from_servers(self):
        self.servers[self.server] = self.user


class Servers(MailClient):
    def __init__(self, server):
        self.server = server
        super().__init__(self, server)

    def all_servers(self):
        return self.servers.keys()

    def receive_mail(self):
        return self.servers[self.server]


class Mail(MailClient):
    def __init__(self, user):
        super().__init__(self, user)

    def send_mail(self, server1, user1, message):
        if server1 not in self.servers:
            return 'Не существующий сервер'
        elif user1 not in self.servers[server1]:
            return 'Не существующий пользователь'
        else:
            return 'Сообщение: ' + message + ' успешно отправлено на сервер ' + \
                   server1 + ' пользователю ' + user1
