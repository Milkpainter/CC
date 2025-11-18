"""
NBA Game Prediction Algorithm
Low Coverage, High Accuracy Model
Base prediction threshold: 50%
"""

class NBAGamePredictor:
    def __init__(self):
        self.confidence_threshold = 53.0
        self.weights = self._initialize_weights()

    def _initialize_weights(self):
        return {
            'win_streak': 5.0,
            'loss_streak': -3.5,
            'recent_form_l5': 2.5,
            'rest_advantage': 3.0,
            'back_to_back_penalty': -6.0,
            'home_court': 2.5,
            'record_differential': 2.0,
            'injury_impact': -4.0,
            'depth_advantage': 2.5,
            'desperation_boost': 3.0,
            'schedule_fatigue': -3.0,
            'momentum_shift': 3.0,
            'head_to_head_recent': 1.0,
            'season_opener_uncertainty': -1.0,
            'overtime_fatigue': -3.0,
            'travel_distance': -1.0,
            'altitude_advantage': 1.5,
            'roster_continuity': 1.2,
            'coaching_change': -2.0,
            'motivation_factor': 1.5
        }

    def calculate_win_streak_score(self, current_streak, is_winning):
        if is_winning:
            if current_streak >= 9:
                return 15.0
            elif current_streak >= 7:
                return 12.0
            elif current_streak >= 5:
                return 9.0
            elif current_streak >= 3:
                return 5.0
            elif current_streak >= 2:
                return 2.5
            return 0.0
        else:
            if current_streak >= 5:
                return -7.0
            elif current_streak >= 3:
                return -4.0
            return 0.0

    def calculate_recent_form_score(self, wins_last_5):
        if wins_last_5 == 5:
            return 8.0
        elif wins_last_5 == 4:
            return 5.0
        elif wins_last_5 == 3:
            return 2.0
        elif wins_last_5 == 2:
            return -1.0
        elif wins_last_5 == 1:
            return -3.0
        else:
            return -5.0

    def calculate_rest_differential_score(self, team_rest_days, opponent_rest_days):
        rest_diff = team_rest_days - opponent_rest_days
        if rest_diff >= 3:
            return 5.0
        elif rest_diff == 2:
            return 3.0
        elif rest_diff == 1:
            return 1.5
        elif rest_diff == -1:
            return -1.5
        elif rest_diff == -2:
            return -3.0
        elif rest_diff <= -3:
            return -5.0
        return 0.0

    def calculate_back_to_back_penalty(self, is_back_to_back, games_in_nights):
        if games_in_nights >= 3:
            return -15.0
        elif is_back_to_back:
            return -7.0
        return 0.0

    def calculate_home_court_advantage(self, is_home):
        return 3.0 if is_home else 0.0

    def calculate_record_differential_score(self, team_wins, team_losses, opp_wins, opp_losses):
        team_total = team_wins + team_losses
        opp_total = opp_wins + opp_losses

        if team_total == 0 or opp_total == 0:
            return 0.0

        team_win_pct = team_wins / team_total
        opp_win_pct = opp_wins / opp_total

        pct_diff = team_win_pct - opp_win_pct

        if pct_diff >= 0.400:
            return 6.0
        elif pct_diff >= 0.300:
            return 4.0
        elif pct_diff >= 0.200:
            return 2.5
        elif pct_diff >= 0.100:
            return 1.0
        elif pct_diff <= -0.400:
            return -6.0
        elif pct_diff <= -0.300:
            return -4.0
        elif pct_diff <= -0.200:
            return -2.5
        elif pct_diff <= -0.100:
            return -1.0
        return 0.0

    def calculate_injury_impact_score(self, missing_starters, missing_rotation_players,
                                     opponent_missing_starters, opponent_missing_rotation):
        team_impact = (missing_starters * 3.0) + (missing_rotation_players * 1.0)
        opp_impact = (opponent_missing_starters * 3.0) + (opponent_missing_rotation * 1.0)

        net_impact = opp_impact - team_impact

        if net_impact >= 9:
            return 7.0
        elif net_impact >= 6:
            return 5.0
        elif net_impact >= 3:
            return 3.0
        elif net_impact <= -9:
            return -7.0
        elif net_impact <= -6:
            return -5.0
        elif net_impact <= -3:
            return -3.0
        return 0.0

    def calculate_depth_advantage_score(self, bench_quality_rating, opponent_bench_quality):
        diff = bench_quality_rating - opponent_bench_quality
        return diff * 1.5

    def calculate_desperation_factor(self, current_record_wins, current_record_losses,
                                    current_streak, is_losing_streak):
        total_games = current_record_wins + current_record_losses
        if total_games == 0:
            return 0.0

        win_pct = current_record_wins / total_games

        if current_record_wins == 0 and total_games >= 2:
            return 5.0

        if is_losing_streak and current_streak >= 3:
            if win_pct < 0.300:
                return 4.0
            elif win_pct < 0.400:
                return 2.5
            return 1.5
        return 0.0

    def calculate_schedule_fatigue_score(self, games_last_7_days, travel_miles_last_week):
        fatigue_score = 0.0

        if games_last_7_days >= 5:
            fatigue_score -= 4.0
        elif games_last_7_days == 4:
            fatigue_score -= 2.0

        if travel_miles_last_week >= 3000:
            fatigue_score -= 2.0
        elif travel_miles_last_week >= 2000:
            fatigue_score -= 1.0

        return fatigue_score

    def calculate_momentum_score(self, recent_wins_margin_avg, recent_losses_margin_avg,
                                trend_direction):
        if trend_direction == 'improving':
            return 3.0
        elif trend_direction == 'declining':
            return -3.0
        return 0.0

    def calculate_overtime_impact(self, played_overtime_recently):
        return -5.0 if played_overtime_recently else 0.0

    def calculate_altitude_advantage(self, is_home, is_high_altitude_venue):
        if is_home and is_high_altitude_venue:
            return 2.0
        elif not is_home and is_high_altitude_venue:
            return -1.5
        return 0.0

    def calculate_roster_continuity_score(self, roster_stability_score):
        return roster_stability_score * 0.5

    def calculate_coaching_impact(self, has_coaching_change, is_interim_coach):
        if is_interim_coach:
            return -3.0
        elif has_coaching_change:
            return -1.5
        return 0.0

    def calculate_motivation_factor(self, is_rivalry_game, is_tournament_game, is_revenge_game):
        motivation = 0.0
        if is_rivalry_game:
            motivation += 1.0
        if is_tournament_game:
            motivation += 1.5
        if is_revenge_game:
            motivation += 1.0
        return motivation

    def calculate_opponent_quality_adjustment(self, recent_opponents_avg_record,
                                             upcoming_opponent_record):
        return 0.0

    def predict_game(self, team_a_data, team_b_data):
        team_a_score = 0.0
        team_b_score = 0.0

        criteria_count = 0

        team_a_score += self.calculate_win_streak_score(
            team_a_data.get('current_streak', 0),
            team_a_data.get('is_winning_streak', False)
        )
        team_b_score += self.calculate_win_streak_score(
            team_b_data.get('current_streak', 0),
            team_b_data.get('is_winning_streak', False)
        )
        criteria_count += 1

        team_a_score += self.calculate_recent_form_score(
            team_a_data.get('wins_last_5', 0)
        )
        team_b_score += self.calculate_recent_form_score(
            team_b_data.get('wins_last_5', 0)
        )
        criteria_count += 1

        rest_score_a = self.calculate_rest_differential_score(
            team_a_data.get('days_rest', 1),
            team_b_data.get('days_rest', 1)
        )
        team_a_score += rest_score_a
        team_b_score -= rest_score_a
        criteria_count += 1

        b2b_penalty_a = self.calculate_back_to_back_penalty(
            team_a_data.get('is_back_to_back', False),
            team_a_data.get('games_in_3_nights', 0)
        )
        b2b_penalty_b = self.calculate_back_to_back_penalty(
            team_b_data.get('is_back_to_back', False),
            team_b_data.get('games_in_3_nights', 0)
        )

        both_on_b2b = (team_a_data.get('is_back_to_back', False) and
                      team_b_data.get('is_back_to_back', False))

        if both_on_b2b:
            if team_a_data.get('is_home', False):
                team_a_score += 3.0
            elif team_b_data.get('is_home', False):
                team_b_score += 3.0

        team_a_score += b2b_penalty_a
        team_b_score += b2b_penalty_b
        criteria_count += 1

        team_a_score += self.calculate_home_court_advantage(
            team_a_data.get('is_home', False)
        )
        team_b_score += self.calculate_home_court_advantage(
            team_b_data.get('is_home', False)
        )
        criteria_count += 1

        record_score = self.calculate_record_differential_score(
            team_a_data.get('wins', 0),
            team_a_data.get('losses', 0),
            team_b_data.get('wins', 0),
            team_b_data.get('losses', 0)
        )
        team_a_score += record_score
        team_b_score -= record_score
        criteria_count += 1

        injury_score = self.calculate_injury_impact_score(
            team_a_data.get('missing_starters', 0),
            team_a_data.get('missing_rotation', 0),
            team_b_data.get('missing_starters', 0),
            team_b_data.get('missing_rotation', 0)
        )
        team_a_score += injury_score
        team_b_score -= injury_score
        criteria_count += 1

        depth_score = self.calculate_depth_advantage_score(
            team_a_data.get('bench_quality', 5),
            team_b_data.get('bench_quality', 5)
        )
        team_a_score += depth_score
        team_b_score -= depth_score
        criteria_count += 1

        team_a_score += self.calculate_desperation_factor(
            team_a_data.get('wins', 0),
            team_a_data.get('losses', 0),
            team_a_data.get('current_streak', 0),
            not team_a_data.get('is_winning_streak', False)
        )
        team_b_score += self.calculate_desperation_factor(
            team_b_data.get('wins', 0),
            team_b_data.get('losses', 0),
            team_b_data.get('current_streak', 0),
            not team_b_data.get('is_winning_streak', False)
        )
        criteria_count += 1

        team_a_score += self.calculate_schedule_fatigue_score(
            team_a_data.get('games_last_7_days', 0),
            team_a_data.get('travel_miles', 0)
        )
        team_b_score += self.calculate_schedule_fatigue_score(
            team_b_data.get('games_last_7_days', 0),
            team_b_data.get('travel_miles', 0)
        )
        criteria_count += 1

        team_a_score += self.calculate_momentum_score(
            team_a_data.get('avg_win_margin', 0),
            team_a_data.get('avg_loss_margin', 0),
            team_a_data.get('trend', 'neutral')
        )
        team_b_score += self.calculate_momentum_score(
            team_b_data.get('avg_win_margin', 0),
            team_b_data.get('avg_loss_margin', 0),
            team_b_data.get('trend', 'neutral')
        )
        criteria_count += 1

        team_a_score += self.calculate_overtime_impact(
            team_a_data.get('played_ot_recently', False)
        )
        team_b_score += self.calculate_overtime_impact(
            team_b_data.get('played_ot_recently', False)
        )
        criteria_count += 1

        altitude_a = self.calculate_altitude_advantage(
            team_a_data.get('is_home', False),
            team_a_data.get('is_high_altitude', False)
        )
        altitude_b = self.calculate_altitude_advantage(
            team_b_data.get('is_home', False),
            team_b_data.get('is_high_altitude', False)
        )
        team_a_score += altitude_a
        team_b_score += altitude_b
        criteria_count += 1

        team_a_score += self.calculate_roster_continuity_score(
            team_a_data.get('roster_stability', 0)
        )
        team_b_score += self.calculate_roster_continuity_score(
            team_b_data.get('roster_stability', 0)
        )
        criteria_count += 1

        team_a_score += self.calculate_coaching_impact(
            team_a_data.get('coaching_change', False),
            team_a_data.get('interim_coach', False)
        )
        team_b_score += self.calculate_coaching_impact(
            team_b_data.get('coaching_change', False),
            team_b_data.get('interim_coach', False)
        )
        criteria_count += 1

        team_a_score += self.calculate_motivation_factor(
            team_a_data.get('is_rivalry', False),
            team_a_data.get('is_tournament', False),
            team_a_data.get('is_revenge', False)
        )
        team_b_score += self.calculate_motivation_factor(
            team_b_data.get('is_rivalry', False),
            team_b_data.get('is_tournament', False),
            team_b_data.get('is_revenge', False)
        )
        criteria_count += 1

        if team_a_data.get('wins', 0) + team_a_data.get('losses', 0) == 0:
            team_a_score -= 4.0
        elif team_a_data.get('wins', 0) + team_a_data.get('losses', 0) <= 2:
            team_a_score -= 2.0

        if team_b_data.get('wins', 0) + team_b_data.get('losses', 0) == 0:
            team_b_score -= 4.0
        elif team_b_data.get('wins', 0) + team_b_data.get('losses', 0) <= 2:
            team_b_score -= 2.0
        criteria_count += 1

        if team_a_data.get('wins', 0) == 0 and team_a_data.get('losses', 0) >= 3:
            team_a_score += 2.0
        if team_b_data.get('wins', 0) == 0 and team_b_data.get('losses', 0) >= 3:
            team_b_score += 2.0
        criteria_count += 1

        total_score_diff = team_a_score - team_b_score

        base_probability = 50.0
        adjusted_probability = base_probability + (total_score_diff * 1.2)

        adjusted_probability = max(0.0, min(100.0, adjusted_probability))

        if abs(total_score_diff) < 2.5:
            return {
                'predicted_winner': None,
                'confidence': 50.0,
                'team_a_probability': 50.0,
                'team_b_probability': 50.0,
                'score_differential': total_score_diff,
                'criteria_evaluated': criteria_count,
                'recommendation': 'NO_PREDICTION'
            }

        if adjusted_probability < self.confidence_threshold and \
           (100 - adjusted_probability) < self.confidence_threshold:
            return {
                'predicted_winner': None,
                'confidence': max(adjusted_probability, 100 - adjusted_probability),
                'team_a_probability': adjusted_probability,
                'team_b_probability': 100 - adjusted_probability,
                'score_differential': total_score_diff,
                'criteria_evaluated': criteria_count,
                'recommendation': 'NO_PREDICTION'
            }

        if adjusted_probability >= 50:
            predicted_winner = 'TEAM_A'
            confidence = adjusted_probability
        else:
            predicted_winner = 'TEAM_B'
            confidence = 100 - adjusted_probability

        return {
            'predicted_winner': predicted_winner,
            'confidence': confidence,
            'team_a_probability': adjusted_probability,
            'team_b_probability': 100 - adjusted_probability,
            'score_differential': total_score_diff,
            'criteria_evaluated': criteria_count,
            'team_a_raw_score': team_a_score,
            'team_b_raw_score': team_b_score,
            'recommendation': 'PREDICT' if confidence >= self.confidence_threshold else 'NO_PREDICTION'
        }


def validate_prediction(predictor, team_a_data, team_b_data, actual_winner, game_description):
    result = predictor.predict_game(team_a_data, team_b_data)

    predicted_winner = result['predicted_winner']
    confidence = result['confidence']

    if predicted_winner is None:
        accuracy = 'ABSTAIN'
        correct = None
    elif predicted_winner == actual_winner:
        accuracy = 'CORRECT'
        correct = True
    else:
        accuracy = 'INCORRECT'
        correct = False

    return {
        'game': game_description,
        'prediction': predicted_winner,
        'actual': actual_winner,
        'confidence': confidence,
        'accuracy': accuracy,
        'correct': correct,
        'team_a_prob': result['team_a_probability'],
        'team_b_prob': result['team_b_probability'],
        'score_diff': result['score_differential']
    }
