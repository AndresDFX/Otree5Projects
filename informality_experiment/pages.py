from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import *
import random, math


# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #

class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_terms']

    def is_displayed(self):
        return self.round_number == 1

#=======================================================================================================================

class GenInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1
#=======================================================================================================================

class Stage1Instructions(Page):

    def is_displayed(self):
        return self.round_number == 1

#=======================================================================================================================

class Stage1Questions(Page):
    form_model = 'player'
    form_fields = [
        'question_1_stage1_instructions',
        'question_2_stage1_instructions',
        'question_3_stage1_instructions',
        'question_4_stage1_instructions'
    ]

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self, values):
        solutions = dict(
            question_1_stage1_instructions='1',
            question_2_stage1_instructions='2',
            question_3_stage1_instructions='2',
            question_4_stage1_instructions='1'
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Respuesta incorrecta, por favor lea de nuevo las instrucciones'

        return error_messages

#=======================================================================================================================
class Stage1Start(Page):

    def is_displayed(self):
        if (self.round_number == 1 or self.round_number == 6 or 
            self.round_number == 11 or self.round_number == 16):
            return True

    def live_method(self, data):
        if self.round_number == 1:
            self.decision_phase_1 = data
        elif self.round_number == 6:
            self.decision_phase_2 = data
        elif self.round_number == 11:
            self.decision_phase_3 = data
        elif self.round_number == 16:
            self.decision_phase_4 = data

#=======================================================================================================================
class Stage1UrnZPreview(Page):

    form_model = 'player'
    form_fields = [
        'question_1_phase1_urnz',
        'question_2_phase1_urnz',
        'question_3_phase1_urnz'
    ]

#=======================================================================================================================
class Stage1Urn(Page):

    def vars_for_template(self):
        num_random = 0
        urn_decision_label = self.player.decision_phase_1
        self.player.token_value_phase_1 = num_random #Numero de ficha aleatoria en cada fase

        return{
            'num_random': num_random,
            'urn_decision_label': urn_decision_label
        }

# ******************************************************************************************************************** #
# *** MANAGEMENT PAGES
# ******************************************************************************************************************** #
#stage_1_sequence = [Consent, GenInstructions, Stage1Instructions, Stage1Questions, Stage1Start, Stage1UrnZPreview, Stage1Urn]
stage_1_sequence = [Stage1Start, Stage1Urn]
page_sequence = stage_1_sequence
