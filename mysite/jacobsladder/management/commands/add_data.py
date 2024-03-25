from datetime import datetime

from django.core.management.base import BaseCommand


from ... import models


class Command(BaseCommand):
    help = 'Add data'

    def handle(self, *arguments, **keywordarguments):
        twenty_ten = datetime(year=2010, month=1, day=1)
        twenty_thirteen = datetime(year=2013, month=1, day=1)
        house_election_2010 = models.HouseElection(election_date=twenty_ten)
        house_election_2010.save()
        house_election_2013 = models.HouseElection(election_date=twenty_thirteen)
        house_election_2013.save()
        seat1 = models.Seat(name="Frank", state=models.StateName.VIC)
        seat1.save()
        seat1.elections.add(house_election_2010)
        seat1.elections.add(house_election_2013)
        seat2 = models.Seat(name="Yossarian", state=models.StateName.VIC)
        seat2.save()
        seat2.elections.add(house_election_2010)
        seat2.elections.add(house_election_2013)
        booth1 = models.Booth()
        booth1.save()
        collection1 = models.Collection(booth=booth1, seat=seat1,
                                        election=house_election_2010)
        collection1.save()
        collection2 = models.Collection(booth=booth1, seat=seat1,
                                        election=house_election_2013)
        collection2.save()
        booth2 = models.Booth()
        booth2.save()
        collection3 = models.Collection(booth=booth2, seat=seat2,
                                        election=house_election_2010)
        collection3.save()
        booth3 = models.Booth()
        booth3.save()
        collection4 = models.Collection(booth=booth3, seat=seat2,
                                        election=house_election_2013)
        collection4.save()
        booth5 = models.Booth()
        booth5.save()
        collection5 = models.Collection(booth=booth5, seat=seat1,
                                        election=house_election_2010)
        collection5.save()
        aap = models.Party(name="Australian Apathy Party", abbreviation="AAP")
        aap.save()
        run = models.Party(name="Running Scared", abbreviation="run")
        run.save()
        guy = models.Person(name="Party Hack")
        guy.save()
        other_guy = models.Person(name="Dangerous Idealogue")
        other_guy.save()
        third_guy = models.Person(name="Narcissist")
        third_guy.save()
        fourth_guy = models.Person(name="Crypto-Fascist")
        fourth_guy.save()
        fifth_guy = models.Person(name="Bored Billionaire")
        fifth_guy.save()
        sixth_guy = models.Person(name="Scandal Magnet")
        sixth_guy.save()
        hack = models.HouseCandidate(person=guy)
        hack.save()
        hack_for_aap_2010 = models.Representation(person=guy, party=aap,
                                                  election=house_election_2010)
        hack_for_aap_2010.save()
        contention1 = models.Contention(candidate=hack, seat=seat1,
                                        election=house_election_2010)
        contention1.save()
        imp = models.HouseCandidate(person=other_guy)
        imp.save()
        imp_for_run_2010 = models.Representation(person=other_guy, party=run,
                                                 election=house_election_2010)
        imp_for_run_2010.save()
        contention2 = models.Contention(candidate=imp, seat=seat1,
                                        election=house_election_2010)
        contention2.save()
        contention3 = models.Contention(candidate=imp, seat=seat1,
                                        election=house_election_2013)
        contention3.save()
        noise = models.HouseCandidate(person=third_guy)
        noise.save()
        noise_for_run_2013 = models.Representation(person=third_guy, party=run,
                                                  election=house_election_2013)
        noise_for_run_2013.save()
        contention4 = models.Contention(candidate=noise, seat=seat1,
                                        election=house_election_2010)
        contention4.save()
        contention5 = models.Contention(candidate=noise, seat=seat2,
                                        election=house_election_2013)
        contention5.save()
        fourth = models.HouseCandidate(person=fourth_guy)
        fourth.save()
        fourth_for_run_2010 = models.Representation(person=fourth_guy, party=run,
                                                   election=house_election_2010)
        fourth_for_run_2010.save()
        contention6 = models.Contention(candidate=fourth, seat=seat2,
                                        election=house_election_2010)
        contention6.save()
        fifth = models.HouseCandidate(person=fifth_guy)
        fifth.save()
        contention7 = models.Contention(candidate=fifth, seat=seat2,
                                        election=house_election_2010)
        contention7.save()
        contention8 = models.Contention(candidate=fifth, seat=seat2,
                                        election=house_election_2013)
        contention8.save()
        sixth = models.HouseCandidate(person=sixth_guy)
        sixth.save()
        sixth_for_aap_2013 = models.Representation(person=sixth_guy, party=aap,
                                                    election=house_election_2013)
        sixth_for_aap_2013.save()
        contention9 = models.Contention(candidate=sixth, seat=seat1,
                                        election=house_election_2013)
        contention9.save()
        tally1 = models.VoteTally(seat=seat1, election=house_election_2010,
                                  candidate=hack, primary_votes=3424, tcp_votes=5006)
        tally1.save()
        tally2 = models.VoteTally(seat=seat1, election=house_election_2010,
                                  candidate=imp, primary_votes=123, tcp_votes=3232)
        tally2.save()
        tally3 = models.VoteTally(seat=seat1, election=house_election_2010,
                                  candidate=noise, primary_votes=45, tcp_votes=0)
        tally3.save()
        tally4 = models.VoteTally(seat=seat1, election=house_election_2013,
                                  candidate=sixth, primary_votes=2345, tcp_votes=4564)
        tally4.save()
        tally5 = models.VoteTally(seat=seat1, election=house_election_2013,
                                  candidate=imp, primary_votes=3453, tcp_votes=6356)
        tally5.save()
        tally6 = models.VoteTally(seat=seat2, election=house_election_2010 ,
                                  candidate=fourth, primary_votes=456, tcp_votes=1456)
        tally6.save()
        tally7 = models.VoteTally(seat=seat2, election=house_election_2010 ,
                                  candidate=fifth, primary_votes=77, tcp_votes=77)
        tally7.save()
        tally8 = models.VoteTally(seat=seat2, election=house_election_2013 ,
                                  candidate=noise, primary_votes=1564, tcp_votes=2075)
        tally8.save()
        tally9 = models.VoteTally(seat=seat2, election=house_election_2013 ,
                                  candidate=fifth, primary_votes=64, tcp_votes=64)
        tally9.save()


