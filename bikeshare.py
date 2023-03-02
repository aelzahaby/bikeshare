import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Choose a city name (chicago, new york city, washington): ").lower()
        cities = ("chicago", "new York city", "washington")
        if city not in cities:
            print("City not valid. Please enter a valid city.")
            continue
        else:
            break
      
    while True:
        month = input("Please choose a month: january, february, march, april, may, june, all: ").lower()
        months = ["january", "february", "march", "april", "may", "june", "all"]
        if month in months:
            break
        else:
            print("Please enter a valid month")


    while True:
        day = input("Please choose a day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all: ").lower()
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
        if day in days:
            break
        else:
            print("Please enter a valid day")
 
    return city, month, day

    print('-'*40)
    


def load_data(city, month, day):
  
    df = pd.read_csv(CITY_DATA[city])
    print(type(df))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    busiest_month = df['month'].mode()
    print(f"our busiest month is {busiest_month}")
    # TO DO: display the most common day of week
    busiest_day = df['day_of_week'].mode()
    print(f"The busiest day is: {busiest_day}")
    # TO DO: display the most common start hour
    busiest_hour = df['hour'].mode()
    print(f"The busiest hour is: {busiest_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    busiest_start_station = df[df['Start Station'].mode()]
    print(f"The busiest start station is: {busiest_start_station}")
    # TO DO: display most commonly used end station
    busiest_end_station = df[df['End Station'].mode()]
    print(f"The busiest end station is: {busiest_end_station}")
    # TO DO: display most frequent combination of start station and end station trip
    group = df.groupby(['Start Station', 'End Station']).count()
    print(f"Most frequent combination of start and end station trips are: {group}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_travel_time}")
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print(f"The average travel time is: {avg_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
    except KeyError:
        print("There is no gender for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
    except KeyError:
        print("No data available for this city")
    try:
        recent_birth_year = df['Birth Year'].max()
    except KeyError:
        print("No data available for this city")
    try:
        most_common_birth_year = df['Birth Year'].mode()
    except KeyError:
        print("No data available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
