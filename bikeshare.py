import time
import pandas as pd
from datetime import timedelta


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
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    City_ID=0
    City_List=['chicago','new york city', 'washington']
    print('Choose City by entering the corresponding number from the list\n')
    while City_ID not in range(1,len(City_List)+1):
               
        for cid in range(len(City_List)):
            print('{}- {}'.format(cid+1,City_List[cid]))
       
        city_answer = input('your choice:')
        
        if city_answer.isdigit():
            City_ID = int(city_answer)
            if City_ID  in range(1,len(City_List)+1):
                city=City_List[City_ID-1]
            else:
                print('You didn\'t choose a valid number, please choose a number between 1 and {}'.format(len(City_List)))
        else:
            print('You didn\'t enter a number, please enter a number between 1 and {}'.format(len(City_List)))
           
      
    # get user input for month (all, january, february, ... , june)
    
    Month_ID=-1
    Month_List=['all','January','February','March','April','May','June']
    print('Would like statistics for certain month, please choose month by entering the corresponding number from the list or 0 for all\n')
    
    while Month_ID not in range(len(Month_List)):
       for mid in range(len(Month_List)): 
           print('{}-{}'.format(mid,Month_List[mid]))
       
       uanswer = input('your choice:')
       if uanswer.isdigit():
           Month_ID=int(uanswer)
           if Month_ID in range(len(Month_List)):
               month=Month_List[Month_ID]
           else:
               print('You didn\'t choose a valid number, please choose a number between 0 and {}'.format(len(Month_List)-1))
       else:
            print('You didn\'t enter a number, please enter a number between 0 and {}'.format(len(Month_List)-1))
           
           

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    Day_ID=-1
    
    Day_List=['all','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    
    print('Would like statistics for certain day, please choose day by entering the corresponding number from the list or 0 for all\n')
    while Day_ID not in range(len(Day_List)):
       for did in range(len(Day_List)): 
           print('{}-{}'.format(did,Day_List[did]))
       
       uanswer = input('your choice:')
       if uanswer.isdigit():
           Day_ID=int(uanswer)
           if Day_ID in range(len(Day_List)):
               day=Day_List[Day_ID]
           else:
               print('You didn\'t choose a valid number, please choose a number between 0 and {}'.format(len(Day_List)-1))
       else:
            print('You didn\'t enter a number, please enter a number between 0 and {}'.format(len(Day_List)-1))


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
    df=pd.read_csv(CITY_DATA[city])
    
    #convert 'start Time' to datetime object
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    # filter based on month then on day
    if month !='all':
        df = df[df['Start Time'].dt.month_name()== month]
        
    if day !='all':
        df = df[df['Start Time'].dt.day_name() == day]
    
           
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
     Args:
        (df)  df - Pandas DataFrame containing city data filtered by month and day if applicable
        
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    
    most_common_month=  df['Start Time'].dt.month_name().mode()[0]  
    print('The most common month is: {}'.format(most_common_month))
    
    # display the most common day of week   
    
    most_common_day=df['Start Time'].dt.day_name().mode()[0]
    print('The most common day of the week is: {}'.format(most_common_day))
 

    # display the most common start hour
    
    most_common_hour=df['Start Time'].dt.hour.mode()[0]    
    print('The most common hour is: {}'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
       (df)  df - Pandas DataFrame containing city data filtered by month and day if applicable
    """
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    df['staion combination']= df['Start Station']+"|"+ df['End Station']
    start_time = time.time()
    most_common_start_station=df['Start Station'].mode()[0]
    most_common_end_station=df['End Station'].mode()[0]
    # display most commonly used start station
    
    print('The most common Start Station is: {}'.format(most_common_start_station))
    
    # display most commonly used end station
    print('The most common End Station is: {}'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df['staion combination'].mode()[0]
    
    print ("most frequent combination of start station and end station : {}".format(most_frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
       df - Pandas DataFrame containing city data filtered by month and day if applicable
    """

    print('\nCalculating Trip Duration statistics...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=float(df['Trip Duration'].sum()) #convert to fload to by pass int64 limitation 
    deltatime = timedelta(seconds=total_travel_time)    
    other_parts=str(deltatime).split(",")[1].split(":")
    print("Total travel time: {:4.2f} secs ,({} days{} hours {} minutes {:4.2f} secs)".format(total_travel_time,deltatime.days,other_parts[0],other_parts[1],float(other_parts[2])))

    
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    
    print("Mean Tavel time time:{:8.2f} secs".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def user_stats(df):
    
    """
    Displays statistics on bikeshare users.
    
    Args:
       df - Pandas DataFrame containing city data filtered by month and day if applicable
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_types = df['User Type'].value_counts()
    
    print("Count of user types:\n{0}\n{1}\n{0}\n".format('-'*20,user_types.to_string()))
    
       
    # Display counts of gender
    
    # check for gender coloumn is missing, other wise print counts of gender
    if 'Gender' in df:
        user_genders = df['Gender'].value_counts()
        print("Count of gender:\n{0}\n{1}\n{0}\n".format('-'*20,user_genders.to_string()))
    else:
       print("There is no Gender data to display for chosen city")     


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_year=df['Birth Year']
        earliest_year_of_birth=int(birth_year.min())
        mostrecent_year_of_birth=int(birth_year.max())
        common_year_of_birth=int(birth_year.mode()[0])
        # year data was collected to calculate age
        data_collection_year=2017 
        
        print("Earliest year of birth:    {} ( eldest user was {} )".format(earliest_year_of_birth,data_collection_year-earliest_year_of_birth))
        print("Most recent year of birth: {} ( youngest user was {} )".format(mostrecent_year_of_birth,data_collection_year-mostrecent_year_of_birth))
        print("Most common year of birth: {} ( most common age {} )".format(common_year_of_birth, data_collection_year-common_year_of_birth))
    
         
    else:
        print("There no Birth Year data to display for chosen city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    
    """
    Displays raw data in batch of 5 upon user request.
    
    Args:
       (df)  df - Pandas DataFrame containing city data filtered by month and day if applicable
       (str) city - name of the city to analyze
    
    """
    
    
        
    reviewanswer = input('\nWould you like to see sample raw data ? (y)es or anything else for no.\n')
    while reviewanswer.lower() == 'yes' or reviewanswer.lower() == 'y':
        
        df = df.sample(5)

        # check if end of data is reached, if so,  exit the loop 
        if df.empty:
            print('no more data to display!')
            break
        else:            
            print(df)
            morereview = input('\nType (y)es if you would you like to see more sample raw data or type anything else for no \n')                
            if morereview.lower() != 'y' and morereview.lower() !='yes':
                break
            

def main():
    while True:
        
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        
        time_stats(df) 
        
        station_stats(df)
        
        trip_duration_stats(df)
        
        user_stats(df)
        show_raw_data(df)

        
        
        restart = input('\nWould you like to restart? Enter (y)es to restart anyother thing to exit.\n')
        if restart.lower() != 'yes' and restart.lower()!='y':
            break
        

if __name__ == "__main__":
	main()