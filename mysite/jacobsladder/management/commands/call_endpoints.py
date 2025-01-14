import pprint
from django.core.management.base import BaseCommand
from ... import endpoints
#import cProfile


class Command(BaseCommand):
    help = "Calls functions in endpoints.py"

    def handle(self, *arguments, **keywordarguments):
        pprint.pp(endpoints.getHouseAttribute(
            elections={'election_date__year': 2022},
            parties={'abbreviation__in': ['ALP'],},
            places={'name__in': ['Wannon']},
            seats=True,
            tally_attribute="postal_votes"
        ))
        exit()

        pprint.pp(endpoints.getHouseAttribute(
            {'election_date__year': 2022},
            {'abbreviation__in': ('GRN', 'GVIC')},
            {'name': 'Wills'},
            tally_attribute="absent_votes"
        ))
        print()
        pprint.pp(endpoints.getHouseAttribute(
            {'election_date__year': 2022},
            {'abbreviation__in': ('GRN', 'GVIC')},
            {'name': 'Wills'},
            tally_attribute="primary_votes"
        ))
        print()
        pprint.pp(endpoints.getHousePrimaryVote(
            {'election_date__year': 2022},
            {'abbreviation__in': ('GRN', 'GVIC')},
            {'name': 'Wills'},
        ))
        print()
        #with cProfile.Profile() as pr:
        pprint.pp(endpoints.getHousePrimaryVote(
            {'election_date__year__in': (2022, 2016, 2010)},
            {'abbreviation__in': ('GRN', 'ALP', 'LP')},
            {'name': 'Aston'},
        ))
            #pr.print_stats()
        print()
        pprint.pp(endpoints.getHousePrimaryVote(
            {'election_date__year__in': (2022, 2016, 2010)},
            {'abbreviation__in': ('GRN', 'ALP', 'LP')},
            {'state__iexact': 'tas'},
        ))
        print()
        pprint.pp(endpoints.getHousePrimaryVote(
            {'election_date__year': 2022},
            {'abbreviation': 'ALP'},
            {'name': 'Chisholm', 'seat__name': 'Bean'},
            False))
        print()
        pprint.pp(endpoints.getHousePrimaryVote(
            {'election_date__year': 2022},
            {'abbreviation': 'ALP'},
            {'name': 'Chisholm',},
            False))
        print()
        pprint.pp(endpoints.getHouseTwoPartyPreferred(
            {'election_date__year__in': (2022, 2016, 2010)},
            {'abbreviation__in': ('GRN', 'ALP', 'LP')},
            {'name': 'Aston'}))
        print()
        pprint.pp(endpoints.getHouseTwoPartyPreferred(
            {'election_date__year': 2022},
            {'abbreviation__in': ('GRN', 'ALP', 'LP')},
            {'name': 'Chisholm', 'seat__name': 'Bean'},
            False))
        print()
        #pprint.pp(endpoints.getHouseGeneralPartyPreferred(
        #    {'election_date__year__in': (2022, 2016, 2010)},
        #    {'name': 'Aston'},
        #    how_many=3))

        pprint.pp(endpoints.getMetaParties())
        print(1)
        endpoints.addMetaParties(
            Libnat={'abbreviation__in': ('LP', 'NP')},
            Green={'abbreviation__in': ('GRN', 'GVIC')},
        )
        pprint.pp(endpoints.getMetaParties())
        print(2)
        endpoints.deleteMetaParties('Libnat')
        print(3)
        pprint.pp(endpoints.getMetaParties())
        print(4)
        endpoints.addMetaParties(Aus={'name__icontains': 'aus'})
        print(5)
        pprint.pp(endpoints.getMetaParties())
        print(6)
        endpoints.deleteMetaParties()
        print(7)
        pprint.pp(endpoints.getMetaParties())
        print(8)
        endpoints.addMetaParties(
            Libnat={'abbreviation__in': ('LP', 'NP')},
            Green={'abbreviation__in': ('GRN', 'GVIC')},
        )
        print(9)
        #pprint.pp(endpoints.getHousePrimaryVote(
        #    {'election_date__year__in': (2022, 2016, )},
        #    {'meta_parties__name': 'Libnat'},
        #    {'state__iexact': 'Vic'}))
        #print(10)
