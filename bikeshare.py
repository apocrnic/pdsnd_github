import time
import pandas as pd
import numpy as np
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Dictionary is a mutable data type that stores mappings of unique keys to values.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington).
    valid_answer = 0
    while valid_answer == 0:
        ask_city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        if ask_city.lower() == 'chicago':
            city = 'chicago'
            valid_answer = 1
        elif ask_city.lower() == 'new york':
            city = 'new york city'
            valid_answer = 1
        elif ask_city.lower() == 'washington':
            city = 'washington'
            valid_answer = 1
        else:
            print("\nYour answer wasn't one of the three choices. Try again.")
            valid_answer = 0
            
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_answer = 0
    while valid_answer == 0:
        ask_month = input('\nWhich month would you like to filter by? January, February, March, April, May, or June? Type "none" for no time filter\n')
        if ask_month.lower() == 'january':
            month = 1
            valid_answer = 1
        elif ask_month.lower() == 'february':
            month = 2
            valid_answer = 1
        elif ask_month.lower() == 'march':
            month = 3
            valid_answer = 1
        elif ask_month.lower() == 'april':
            month = 4
            valid_answer = 1
        elif ask_month.lower() == 'may':
            month = 5
            valid_answer = 1
        elif ask_month.lower() == 'june':
            month = 6
            valid_answer = 1     
        elif ask_month.lower() == 'none':
            month = 100
            valid_answer = 1              
        else:
            print("\nYour answer wasn't one of the six choices. Try again.")
            valid_answer = 0

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_answer = 0
    while valid_answer == 0:
        ask_day = input('\nWhich day? Please type your response as an integer (e.g. 1 = Sunday).Type "none" for no day filter\n')
        if ask_day == '1':
            day = 6
            valid_answer = 1
        elif ask_day == '2':
            day = 0
            valid_answer = 1
        elif ask_day == '3':
            day = 1
            valid_answer = 1
        elif ask_day == '4':
            day = 2
            valid_answer = 1
        elif ask_day == '5':
            day = 3
            valid_answer = 1
        elif ask_day == '6':
            day = 4
            valid_answer = 1
        elif ask_day == '7':
            day = 5
            valid_answer = 1     
        elif ask_day == 'none':
            day = 100
            valid_answer = 1                  
        else:
            print("\nYour answer wasn't one of the 7 integer choices available. Try again.")
            valid_answer = 0

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
    
    # extract month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['month_full_name'] = df['Start Time'].dt.month_name()

    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week_integer'] = df['Start Time'].dt.weekday    
   
    if day != 100:
        df = df[df['day_of_week_integer'] == day]
    if month != 100:
            df = df[df['month'] == month]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    number_of_appearances_hour = df['hour'].value_counts().max()
    
     # find the most popular day
    popular_day = df['day_of_week'].mode()[0]
    number_of_appearances_day = df['day_of_week'].value_counts().max()
    
    # find the most popular month
    popular_month = df['month_full_name'].mode()[0]
    number_of_appearances_month = df['month_full_name'].value_counts().max()
     
    print('The most popular start hour:', popular_hour, ', Count:', number_of_appearances_hour)
    if day == 100:
            print('The most popular day of the week is:', popular_day, ', Count:', number_of_appearances_day)
    if month == 100:
            print('The most popular month is:', popular_month, ', Count:', number_of_appearances_month)
    return df

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    number_of_appearances_start_station = df['Start Station'].value_counts().max()
    print('The most popular starting station:', popular_start_station, ', Count:', number_of_appearances_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    number_of_appearances_end_station = df['End Station'].value_counts().max()
    print('The most popular ending station:', popular_end_station, ', Count:', number_of_appearances_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station','End Station']).size().idxmax()
    count_popular_trip = df.groupby(['Start Station','End Station']).size().sort_values(ascending = False)[0]
    
    print('The most popular trip:', popular_trip, ', Count:', count_popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #TO DO: display total travel time
    df['Elapsed_Time'] = df['End Time']-df['Start Time']
    total_travel_time = df['Elapsed_Time'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Elapsed_Time'].mean()

    print('Given the filters you provided, the total travel time was: ', total_travel_time, ' and the average_travel_time was: ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('The breakdown of users is: \n', user_type_counts)
    

    if city != "washington":
        # TO DO: Display counts of gender
        gender_type_counts = df['Gender'].value_counts()
        print('\nThe breakdown of genders is: \n', gender_type_counts)
        # TO DO: Display earliest, most recent, and most common year of birth
        popular_birth_year = df['Birth Year'].mode()[0]
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        print('\nThe oldest, youngest, and most popular year of birth, respectively are: \n', int(oldest), ', ', int(youngest), ' and ', int(popular_birth_year))
    else:
        print('\nThere are no gender or birth year statistics for the city of Washingtion.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    # TO DO: get user input for whether they would like to see 5 lines of raw data
    lines_to_display = 5
    counter = 1
    while True:
        if counter == 1:
            raw_data = input('Would you like to see 5 rows of raw data?\nPlease select yes or no. ').lower()
            counter = 2
        else:
            raw_data = input('Would you like to see 5 more rows of raw data?\nPlease select yes or no. ').lower()
            
        if (raw_data == 'yes'):
            print(df.iloc[lines_to_display-5:lines_to_display],'\n')
            lines_to_display+=5
            continue
        elif (raw_data == 'no'):
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
