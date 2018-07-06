import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    cond = 0
    while cond != 1:
        city = input("Which city would you like? ")
        city = city.lower()
        if city in cities:
            cond = 1
        else:
            cond = 0


        # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all' , 'january','february','march','april','may','june','july','august','september''october','november','december']
    cond = 0
    while cond != 1:
        month = input("Which month would you like? ")
        month = month.lower()
        if month in months:
            cond = 1
        else:
            cond = 0

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    cond = 0
    while cond != 1:
        day = input("Which day would you like? ")
        day = day.lower()
        if day in days:
            cond = 1
        else:
            cond = 0


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
    #print(df)    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
  
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    index = int(df['Start Time'].dt.month.mode())
   
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[index - 1]
    
    print('The most popular month is {}.'.format(most_common_month)) 


    # display the most common day of week
    index = int(df['Start Time'].dt.weekday.mode())
   
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 
    most_common_day = weekdays[index - 1]
   
    print('The most popular day of week is {}.'.format(most_common_day)) 


    # display the most common start hour
    common_start_hour= int(df['Start Time'].dt.hour.mode())
#     most_common_month = months[index - 1]
#     print(most_common_month)
    if common_start_hour == 0:
        am_pm = 'AM'
        common_start_hour_read = 12
    elif 1 <= common_start_hour < 13:
        am_pm = 'AM'
        common_start_hour_read = common_start_hour
    elif 13 <= common_start_hour < 24:
        am_pm = 'PM'
        common_start_hour_read = common_start_hour - 12
    print('The most popular hour of day for start time is {} {}.'.format(common_start_hour_read, am_pm))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    used_start_station = df ['Start Station'].mode()[0]
    print('The most commonly used start station is {}.'.format(used_start_station)) 
    
    # display most commonly used end station
    used_end_station = df ['End Station'].mode()[0]
    print('The most commonly used end station is {}.'.format(used_end_station)) 

    # display most frequent combination of start station and end station trip
    #startend = df[df['Start Station'], df['End Station'].value_counts()]
    df['startend'] = df['Start Station'].str.cat(df['End Station'], sep=' to ') 
    most_pop_trip = df['startend'].mode()[0]
    print('The most frequent station combination of start station and end station trip is {}.'.format(most_pop_trip)) 
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = df ['Trip Duration'].sum()
   
    print('The total trip duration is {} seconds.'.format(trip_duration)) 

    minute, second = divmod(trip_duration, 60)
  
    print('The total trip duration is {} minutes and {} seconds.'.format(minute,second)) 

    hours, minutes = divmod(minute,60)
   
    print('The total trip duration is {} hours and {} minutes.'.format(hours, minutes)) 

    day, hours =divmod(hours,24)

    
    print('The total trip duration is {} days and {} hours.'.format(day, hours)) 

    # display mean travel time
    avg_trip_duration = int(round(df ['Trip Duration'].mean()))
  
    m, s = divmod(avg_trip_duration, 60)
    if m > 60 :
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}' ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))       
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    #df.domain.value_counts()
    count_user_types = df ['User Type'].value_counts()
    print('The counts of user types are {}.'.format(count_user_types)) 


    # Display counts of gender
    gender = df ['Gender'].value_counts()
    print('The counts of gender are {}.'.format(gender)) 

    # Display earliest, most recent, and most common year of birth
    earliest_year = int(df ['Birth Year'].min())
    
    recent_year = int(df ['Birth Year'].max())
    
    common_year =int(df ['Birth Year'].mode())
  
    print('The earliest year is {}, most recent year is {} and most common year of birth {}.'.format(earliest_year,recent_year,common_year ))       
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city,month,day = get_filters()
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


