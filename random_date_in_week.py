def random_date_in_week(year, week_number):
    first_day = datetime.strptime(f'{year}-W{week_number}-1', '%Y-W%W-%w')
    random_days = random.randint(0, 6)
    random_date = first_day + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')