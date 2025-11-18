"""
Test NBA Prediction Algorithm on All 37 Games
Includes comprehensive pre-game data for each matchup
"""

from nba_prediction_algorithm import NBAGamePredictor, validate_prediction

def run_all_predictions():
    predictor = NBAGamePredictor()
    results = []

    game1_gsw = {
        'wins': 1, 'losses': 0, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': True, 'games_in_3_nights': 2,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 3,
        'bench_quality': 6, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 0
    }
    game1_den = {
        'wins': 0, 'losses': 0, 'current_streak': 0, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 10, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 7, 'games_last_7_days': 0, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': True,
        'roster_stability': 7, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 0
    }
    results.append(validate_prediction(predictor, game1_gsw, game1_den, 'TEAM_A',
                                      'Oct 23: GSW vs DEN (OT)'))

    game2_lal = {
        'wins': 0, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 1, 'missing_rotation': 3,
        'bench_quality': 5, 'games_last_7_days': 1, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': True,
        'avg_win_margin': 0, 'avg_loss_margin': 10
    }
    game2_min = {
        'wins': 1, 'losses': 0, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 1, 'travel_miles': 1000,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 0
    }
    results.append(validate_prediction(predictor, game2_lal, game2_min, 'TEAM_A',
                                      'Oct 24: LAL vs MIN'))

    game3_mil = {
        'wins': 1, 'losses': 0, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 1,
        'bench_quality': 6, 'games_last_7_days': 1, 'travel_miles': 500,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 0
    }
    game3_tor = {
        'wins': 1, 'losses': 0, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 1,
        'bench_quality': 5, 'games_last_7_days': 1, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 20, 'avg_loss_margin': 0
    }
    results.append(validate_prediction(predictor, game3_mil, game3_tor, 'TEAM_A',
                                      'Oct 24: MIL vs TOR'))

    game4_por = {
        'wins': 0, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 3,
        'bench_quality': 4, 'games_last_7_days': 1, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 3, 'coaching_change': True, 'interim_coach': True,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 10
    }
    game4_gsw = {
        'wins': 2, 'losses': 0, 'current_streak': 2, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 3,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 6, 'games_last_7_days': 3, 'travel_miles': 800,
        'trend': 'improving', 'played_ot_recently': True, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 0
    }
    results.append(validate_prediction(predictor, game4_por, game4_gsw, 'TEAM_A',
                                      'Oct 24: POR vs GSW'))

    game5_mia = {
        'wins': 1, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 1,
        'bench_quality': 5, 'games_last_7_days': 2, 'travel_miles': 1000,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 10
    }
    game5_mem = {
        'wins': 1, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 7,
        'bench_quality': 3, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 3, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 12
    }
    results.append(validate_prediction(predictor, game5_mia, game5_mem, 'TEAM_A',
                                      'Oct 24: MIA vs MEM'))

    game6_dal = {
        'wins': 0, 'losses': 2, 'current_streak': 2, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 1, 'missing_rotation': 3,
        'bench_quality': 4, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 8
    }
    game6_tor = {
        'wins': 1, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 2, 'missing_rotation': 3,
        'bench_quality': 4, 'games_last_7_days': 2, 'travel_miles': 2000,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 20, 'avg_loss_margin': 6
    }
    results.append(validate_prediction(predictor, game6_dal, game6_tor, 'TEAM_A',
                                      'Oct 26: DAL vs TOR'))

    game7_cha = {
        'wins': 0, 'losses': 2, 'current_streak': 2, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 2, 'travel_miles': 400,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 8
    }
    game7_was = {
        'wins': 0, 'losses': 2, 'current_streak': 2, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 4, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game7_cha, game7_was, 'TEAM_A',
                                      'Oct 26: CHA vs WAS'))

    game8_det = {
        'wins': 2, 'losses': 0, 'current_streak': 2, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 0
    }
    game8_bos = {
        'wins': 0, 'losses': 3, 'current_streak': 3, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 4, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 700,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 3, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game8_det, game8_bos, 'TEAM_A',
                                      'Oct 26: DET vs BOS'))

    game9_uta = {
        'wins': 1, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': True,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 21, 'avg_loss_margin': 1
    }
    game9_phx = {
        'wins': 1, 'losses': 2, 'current_streak': 2, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 1,
        'bench_quality': 5, 'games_last_7_days': 2, 'travel_miles': 600,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 15
    }
    results.append(validate_prediction(predictor, game9_uta, game9_phx, 'TEAM_A',
                                      'Oct 27: UTA vs PHX (OT)'))

    game10_cle = {
        'wins': 2, 'losses': 0, 'current_streak': 2, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 2, 'travel_miles': 100,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 7, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 0
    }
    game10_det = {
        'wins': 2, 'losses': 1, 'current_streak': 3, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 3, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 0
    }
    results.append(validate_prediction(predictor, game10_cle, game10_det, 'TEAM_A',
                                      'Oct 27: CLE vs DET'))

    game11_chi = {
        'wins': 1, 'losses': 1, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 5
    }
    game11_atl = {
        'wins': 1, 'losses': 2, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 700,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game11_chi, game11_atl, 'TEAM_A',
                                      'Oct 27: CHI vs ATL'))

    game12_gsw = {
        'wins': 2, 'losses': 1, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 4, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 6, 'games_last_7_days': 3, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': True, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 20
    }
    game12_lac = {
        'wins': 1, 'losses': 2, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 400,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 12
    }
    results.append(validate_prediction(predictor, game12_gsw, game12_lac, 'TEAM_A',
                                      'Oct 28: GSW vs LAC'))

    game13_mil = {
        'wins': 2, 'losses': 1, 'current_streak': 2, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 4, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 2, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 5
    }
    game13_nyk = {
        'wins': 2, 'losses': 2, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 4, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 3, 'travel_miles': 800,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game13_mil, game13_nyk, 'TEAM_A',
                                      'Oct 28: MIL vs NYK'))

    game14_det = {
        'wins': 3, 'losses': 2, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 4, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 10
    }
    game14_orl = {
        'wins': 1, 'losses': 3, 'current_streak': 4, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 4, 'travel_miles': 1000,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game14_det, game14_orl, 'TEAM_A',
                                      'Oct 29: DET vs ORL'))

    game15_mem = {
        'wins': 2, 'losses': 2, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 4,
        'bench_quality': 4, 'games_last_7_days': 3, 'travel_miles': 1000,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 10
    }
    game15_phx = {
        'wins': 1, 'losses': 3, 'current_streak': 3, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 1, 'missing_rotation': 1,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': True, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 13
    }
    results.append(validate_prediction(predictor, game15_mem, game15_phx, 'TEAM_A',
                                      'Oct 29: MEM vs PHX'))

    game16_por = {
        'wins': 2, 'losses': 2, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 800,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': True,
        'roster_stability': 4, 'coaching_change': True, 'interim_coach': True,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 10
    }
    game16_uta = {
        'wins': 2, 'losses': 2, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': True, 'is_high_altitude': True,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 25, 'avg_loss_margin': 3
    }
    results.append(validate_prediction(predictor, game16_por, game16_uta, 'TEAM_A',
                                      'Oct 29: POR vs UTA'))

    game17_bos = {
        'wins': 1, 'losses': 2, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 3, 'travel_miles': 400,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 6, 'avg_loss_margin': 10
    }
    game17_phi = {
        'wins': 0, 'losses': 3, 'current_streak': 3, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 5
    }
    results.append(validate_prediction(predictor, game17_bos, game17_phi, 'TEAM_A',
                                      'Oct 30: BOS vs PHI'))

    game18_lal = {
        'wins': 1, 'losses': 2, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 3,
        'bench_quality': 5, 'games_last_7_days': 2, 'travel_miles': 500,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 8
    }
    game18_mem = {
        'wins': 3, 'losses': 2, 'current_streak': 2, 'is_winning_streak': True,
        'wins_last_5': 3, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 4,
        'bench_quality': 4, 'games_last_7_days': 4, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game18_lal, game18_mem, 'TEAM_A',
                                      'Oct 31: LAL vs MEM'))

    game19_atl = {
        'wins': 2, 'losses': 3, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 4, 'travel_miles': 500,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 10
    }
    game19_ind = {
        'wins': 0, 'losses': 4, 'current_streak': 4, 'is_winning_streak': False,
        'wins_last_5': 0, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 4, 'missing_rotation': 4,
        'bench_quality': 3, 'games_last_7_days': 4, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 2, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 0, 'avg_loss_margin': 15
    }
    results.append(validate_prediction(predictor, game19_atl, game19_ind, 'TEAM_A',
                                      'Oct 31: ATL vs IND'))

    game20_cha = {
        'wins': 1, 'losses': 5, 'current_streak': 3, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 2, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 4, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 26, 'avg_loss_margin': 10
    }
    game20_uta = {
        'wins': 2, 'losses': 4, 'current_streak': 3, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 5, 'travel_miles': 2500,
        'trend': 'declining', 'played_ot_recently': True, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 25, 'avg_loss_margin': 5
    }
    results.append(validate_prediction(predictor, game20_cha, game20_uta, 'TEAM_A',
                                      'Nov 2: CHA vs UTA'))

    game21_chi = {
        'wins': 2, 'losses': 3, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 4, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    game21_phi = {
        'wins': 1, 'losses': 4, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 4, 'travel_miles': 700,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 1, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game21_chi, game21_phi, 'TEAM_A',
                                      'Nov 4: CHI vs PHI'))

    game22_tor = {
        'wins': 3, 'losses': 2, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 4, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 10
    }
    game22_mil = {
        'wins': 3, 'losses': 3, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 5, 'travel_miles': 800,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game22_tor, game22_mil, 'TEAM_A',
                                      'Nov 4: TOR vs MIL'))

    game23_no = {
        'wins': 3, 'losses': 3, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 5, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 8
    }
    game23_cha = {
        'wins': 2, 'losses': 5, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 2, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 5, 'travel_miles': 700,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game23_no, game23_cha, 'TEAM_A',
                                      'Nov 4: NO vs CHA'))

    game24_lal = {
        'wins': 2, 'losses': 3, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 1, 'missing_rotation': 3,
        'bench_quality': 5, 'games_last_7_days': 3, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 10
    }
    game24_sas = {
        'wins': 2, 'losses': 4, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 5, 'travel_miles': 1500,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game24_lal, game24_sas, 'TEAM_A',
                                      'Nov 5: LAL vs SAS'))

    game25_sac = {
        'wins': 4, 'losses': 4, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 6, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 8
    }
    game25_gsw = {
        'wins': 4, 'losses': 5, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 6, 'games_last_7_days': 7, 'travel_miles': 100,
        'trend': 'declining', 'played_ot_recently': True, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game25_sac, game25_gsw, 'TEAM_A',
                                      'Nov 5: SAC vs GSW'))

    game26_phx = {
        'wins': 3, 'losses': 5, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 6, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 10
    }
    game26_lac = {
        'wins': 3, 'losses': 5, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 7, 'travel_miles': 400,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 12
    }
    results.append(validate_prediction(predictor, game26_phx, game26_lac, 'TEAM_A',
                                      'Nov 6: PHX vs LAC'))

    game27_tor = {
        'wins': 5, 'losses': 3, 'current_streak': 2, 'is_winning_streak': True,
        'wins_last_5': 4, 'days_rest': 3, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 5, 'travel_miles': 1000,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 8
    }
    game27_atl = {
        'wins': 4, 'losses': 4, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 6, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game27_tor, game27_atl, 'TEAM_A',
                                      'Nov 7: TOR vs ATL'))

    game28_mia = {
        'wins': 5, 'losses': 4, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 1, 'missing_rotation': 0,
        'bench_quality': 7, 'games_last_7_days': 7, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 8
    }
    game28_por = {
        'wins': 3, 'losses': 6, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 7, 'travel_miles': 3000,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': True, 'interim_coach': True,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 5
    }
    results.append(validate_prediction(predictor, game28_mia, game28_por, 'TEAM_A',
                                      'Nov 8: MIA vs POR'))

    game29_orl = {
        'wins': 2, 'losses': 7, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 7, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 10
    }
    game29_por = {
        'wins': 3, 'losses': 7, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 2, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 8, 'travel_miles': 2500,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': True, 'interim_coach': True,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game29_orl, game29_por, 'TEAM_A',
                                      'Nov 9: ORL vs POR'))

    game30_phx = {
        'wins': 6, 'losses': 5, 'current_streak': 4, 'is_winning_streak': True,
        'wins_last_5': 4, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 7, 'travel_miles': 1000,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 5
    }
    game30_dal = {
        'wins': 3, 'losses': 9, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 1, 'missing_rotation': 2,
        'bench_quality': 4, 'games_last_7_days': 9, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 5, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game30_phx, game30_dal, 'TEAM_A',
                                      'Nov 12: PHX vs DAL'))

    game31_cha = {
        'wins': 4, 'losses': 7, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 2, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 2, 'missing_rotation': 3,
        'bench_quality': 6, 'games_last_7_days': 8, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 8
    }
    game31_mil = {
        'wins': 7, 'losses': 5, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 9, 'travel_miles': 1000,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game31_cha, game31_mil, 'TEAM_A',
                                      'Nov 12: CHA vs MIL'))

    game32_det = {
        'wins': 10, 'losses': 2, 'current_streak': 8, 'is_winning_streak': True,
        'wins_last_5': 5, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 4, 'missing_rotation': 3,
        'bench_quality': 7, 'games_last_7_days': 8, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 5
    }
    game32_chi = {
        'wins': 6, 'losses': 5, 'current_streak': 4, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 9, 'travel_miles': 250,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game32_det, game32_chi, 'TEAM_A',
                                      'Nov 12: DET vs CHI'))

    game33_atl = {
        'wins': 8, 'losses': 5, 'current_streak': 4, 'is_winning_streak': True,
        'wins_last_5': 4, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 1,
        'bench_quality': 7, 'games_last_7_days': 9, 'travel_miles': 2000,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': True,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 8
    }
    game33_uta = {
        'wins': 3, 'losses': 7, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 1, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 5, 'games_last_7_days': 7, 'travel_miles': 0,
        'trend': 'declining', 'played_ot_recently': False, 'is_high_altitude': True,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 25, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game33_atl, game33_uta, 'TEAM_A',
                                      'Nov 13: ATL vs UTA'))

    game34_det = {
        'wins': 11, 'losses': 2, 'current_streak': 9, 'is_winning_streak': True,
        'wins_last_5': 5, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 4, 'missing_rotation': 2,
        'bench_quality': 7, 'games_last_7_days': 9, 'travel_miles': 0,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 5
    }
    game34_phi = {
        'wins': 7, 'losses': 5, 'current_streak': 1, 'is_winning_streak': True,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 3, 'missing_rotation': 0,
        'bench_quality': 5, 'games_last_7_days': 9, 'travel_miles': 500,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': True, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game34_det, game34_phi, 'TEAM_A',
                                      'Nov 14: DET vs PHI'))

    game35_lal = {
        'wins': 4, 'losses': 7, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 2, 'days_rest': 0, 'is_back_to_back': True, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 1, 'missing_rotation': 3,
        'bench_quality': 5, 'games_last_7_days': 9, 'travel_miles': 1000,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 4, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 15, 'avg_loss_margin': 10
    }
    game35_mil = {
        'wins': 8, 'losses': 6, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 0, 'is_back_to_back': True, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 11, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 8, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game35_lal, game35_mil, 'TEAM_A',
                                      'Nov 15: LAL vs MIL'))

    game36_den = {
        'wins': 7, 'losses': 4, 'current_streak': 7, 'is_winning_streak': True,
        'wins_last_5': 5, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 0, 'missing_rotation': 2,
        'bench_quality': 6, 'games_last_7_days': 7, 'travel_miles': 800,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 5
    }
    game36_min = {
        'wins': 8, 'losses': 5, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 1,
        'bench_quality': 6, 'games_last_7_days': 10, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': True, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 8
    }
    results.append(validate_prediction(predictor, game36_den, game36_min, 'TEAM_A',
                                      'Nov 15: DEN vs MIN'))

    game37_atl = {
        'wins': 9, 'losses': 6, 'current_streak': 5, 'is_winning_streak': True,
        'wins_last_5': 5, 'days_rest': 3, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': False, 'missing_starters': 2, 'missing_rotation': 2,
        'bench_quality': 7, 'games_last_7_days': 10, 'travel_miles': 1500,
        'trend': 'improving', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 6, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 12, 'avg_loss_margin': 8
    }
    game37_phx = {
        'wins': 7, 'losses': 6, 'current_streak': 1, 'is_winning_streak': False,
        'wins_last_5': 3, 'days_rest': 1, 'is_back_to_back': False, 'games_in_3_nights': 0,
        'is_home': True, 'missing_starters': 0, 'missing_rotation': 0,
        'bench_quality': 6, 'games_last_7_days': 10, 'travel_miles': 0,
        'trend': 'neutral', 'played_ot_recently': False, 'is_high_altitude': False,
        'roster_stability': 5, 'coaching_change': False, 'interim_coach': False,
        'is_rivalry': False, 'is_tournament': False, 'is_revenge': False,
        'avg_win_margin': 10, 'avg_loss_margin': 10
    }
    results.append(validate_prediction(predictor, game37_atl, game37_phx, 'TEAM_A',
                                      'Nov 16: ATL vs PHX'))

    return results


if __name__ == "__main__":
    print("=" * 80)
    print("NBA PREDICTION ALGORITHM - TESTING ALL 37 GAMES")
    print("=" * 80)
    print()

    results = run_all_predictions()

    correct_predictions = 0
    incorrect_predictions = 0
    abstentions = 0

    print("\nDETAILED RESULTS:")
    print("-" * 80)

    for i, result in enumerate(results, 1):
        status_symbol = ""
        if result['accuracy'] == 'CORRECT':
            status_symbol = "✓"
            correct_predictions += 1
        elif result['accuracy'] == 'INCORRECT':
            status_symbol = "✗"
            incorrect_predictions += 1
        else:
            status_symbol = "○"
            abstentions += 1

        print(f"{i:2d}. {status_symbol} {result['game']}")
        print(f"    Predicted: {result['prediction']} ({result['confidence']:.1f}%) | "
              f"Actual: {result['actual']} | Status: {result['accuracy']}")
        print(f"    Team A: {result['team_a_prob']:.1f}% | Team B: {result['team_b_prob']:.1f}%")
        print()

    total_predictions_made = correct_predictions + incorrect_predictions
    accuracy_rate = (correct_predictions / total_predictions_made * 100) if total_predictions_made > 0 else 0

    print("=" * 80)
    print("FINAL STATISTICS:")
    print("=" * 80)
    print(f"Total Games: {len(results)}")
    print(f"Predictions Made: {total_predictions_made}")
    print(f"Correct: {correct_predictions}")
    print(f"Incorrect: {incorrect_predictions}")
    print(f"Abstained: {abstentions}")
    print(f"Accuracy Rate: {accuracy_rate:.1f}% (of games predicted)")
    print(f"Coverage: {(total_predictions_made / len(results) * 100):.1f}%")
    print("=" * 80)
