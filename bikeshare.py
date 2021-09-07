import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Kindly select a city!')
    city = None
    while city not in ('Washington', 'New York City', 'Chicago'):
        try:
            city = input('Kindly type Chicago, New York City or Washington : ').lower().title()

        except KeyboardInterrupt:
            print('Keyboard interrupt')

    print('You have selected ' + city)

    # TO DO: get user input for month (all, january, february, ... , june)

    print('Kindly select a month')
    month = None
    while month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        try:
            month=input('Kindly type the month name (name must be capitalized and must fall within January to June) or type "all" if you want to view all the months : ').lower().title()

        except KeyboardInterrupt:
            print('Keyboard interrupt')

    print('You have selected ' + month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('Kindly select a day within the week')
    day=None
    while day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
        try:
            day=input('Kindly type the day of the week (name must be capitalized and must fall within Sunday to Saturday) or type "all" if you would like to see all the weekdays : ').lower().title()

        except KeyboardInterrupt:
            print('Keyboard interrupt')

    print('You have selected ' + day)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'All':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    months_list = ['empty', 'January', 'February', 'March', 'April', 'May', 'June']
    popular_month = df['month'].mode()[0]
    print('The most Popular Month: ' + months_list[popular_month])

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('The most Popular Weekday: ' + popular_day)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column

    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour

    popular_hour = df['hour'].mode()[0]
    print('The most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds to complete." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular Start Station: ' + popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular End Station: ' + popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    # create a trip column from start station and end station

    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('The most popular trip was from ' + popular_trip)
    print("\nThis took %s seconds to complete." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_s = df['Trip Duration'].sum(skipna=True)
    total_travel_time_h = float(total_travel_time_s) / 3600
    print('The total travel time was ' + str(total_travel_time_s) + ' seconds, which is equivalent to ' + str(total_travel_time_h) + ' hours.')
   
    # TO DO: display mean travel time
    mean_travel_time_s = df['Trip Duration'].mean(skipna=True)
    mean_travel_time_m = mean_travel_time_s / 60
    print('The average travel time was ' + str(mean_travel_time_s) + ' seconds, which is equivalent to ' + str(mean_travel_time_m) + ' minutes.')
    print("\nThis took %s seconds to complete." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The number of the User Types are:\n' + str(user_types) + '\n')

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('The number of the Genders are:\n' + str(genders) + '\n')
    except:
        print('The number of the Genders are:\nNo data for this city.' + '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min(skipna=True)
        recent_birth_year = df['Birth Year'].max(skipna=True)
        frequent_birth_year = df['Birth Year'].mode()[0]
        print('The earliest birth year was ' + str(earliest_birth_year) + ', the most recent birth year was ' + str(recent_birth_year) + ' and the most frequent birth year was ' + str(frequent_birth_year))

    except:
        print("No data available for this city's birth year")

    print("\nThis took %s seconds to complete." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        try:
            row=0
            raw_data = input('Do you want to view the raw data? Type yes or no. ').lower()

            while True:
                if raw_data == 'no':
                    break

                elif raw_data == 'yes':
                    print(df.iloc[row:row+5])
                    row=row+5
                    raw_data = input('Do you want to view more raw data? Type yes or no. ').lower()

                else:
                    print('Please type yes or no!')
                    raw_data = input('Do you want to see more raw data? Type yes or no. ').lower()

        except KeyboardInterrupt:
            print('Keyboard interrupt')
            
        restart = input('\nDo you want to restart the whole process? Type yes or no.\n')

        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()