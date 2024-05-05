from django.core.management.base import BaseCommand
from ... import models


class Command(BaseCommand):
    help = "Look at these N seats. How do preferences flow from the Libs to " \
           "ALP/Greens in the 2016 election, and how about 2022 (where the " \
           "Lib recommendation was different?)\n\n"

    AEC_RESULTS = {}

    def handle(self, *arguments, **keywordarguments):
        print(Command.help)
        print("\n")




