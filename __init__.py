from mycroft import MycroftSkill, intent_file_handler


class NavigationSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.navigation.intent')
    def handle_skill_navigation(self, message):
        self.speak_dialog('skill.navigation')


def create_skill():
    return NavigationSkill()

