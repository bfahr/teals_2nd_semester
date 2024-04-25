"""
Unit 6 Project - Song Database
==============================

In this project you will be reading data from a string to start your database.
The data is in CSV (Comma Separated Values) format [1]. This means that each line of the
string will contain an artist name, a song title, and an album title, separated by commas.
The provided function read_song_db read that data into a list. Each line
of the list will look like this:

    "Michael Jackson,Billie Jean,Thriller"

The first line of the file usually contains the column names, in this case that would be

    "artist,song title,album"

Spreadsheet programs can read and write CSV files, and it is a common format for data
provided on the internet.

[1] https://en.wikipedia.org/wiki/Comma-separated_values

Part 1
------

Implement the load_initial_db function to split each line of data to get artist, song and album
and save the information in a database that is a dictionary.  You may structure the dictionary
any way you choose. Read through the rest of the Project description to make sure you understand
how you will be accessing the data.  That should influence how you structure your dictionary
database.

Part 2
------

Add the following capabilities using the template functions provided in the sample code to your
game loop:

    - Print the commands (help)
    - Print the information in the database
    - Print the artists names
    - Print the album names
    - Find all songs by an artist name (find_artist_songs)
    - Find a song title that contains specified text (find_songs_like)
    - Quit the program

Part 3
------

    - Add the capability to add a new song to the database.
    - Add the capability to remove a song from the database.

Part 4
------

Add the ability to save your song database using the backup_db function.  This will
save the song database dictionary into a file with the name "song_db.json". JavaScript Object
Notation (JSON) [2] is a lightweight data interchange format and built into Python.  JSON files
can be read by most other programming languages as well as many tools, including web browsers.
Open the file manager in PythonAnywhere and open this file after you have backed it up.

Once you have backed up your song database, use the restore_db function to restore the song
database dictionary.  Print all the records and make sure the object has the same information.

[2] https://www.json.org/json-en.html

Bonus
-----

Add functionality to store a genre [3] and a song rating in the database.  Genre is a category
that classifies a song based on various criteria.  Examples of genres include "rock", "country",
and "pop", but there are literally hundreds of genres and subgenres. The song rating is typically
a set of stars "*" from 1-5, but you can choose whatever type of rating system you like.

[3] https://en.wikipedia.org/wiki/Music_genre
"""
import json
import os

# Sample starting data for this project
# This is a single string with embedded End-of-Line (EOL) chars at the end of each line
# .strip() at the end of the string removes any extra whitespace at the beginning and end of the string
SAMPLE_CSV_DATA = """
Artist,Song,Album
Taylor Swift,Welcome To New York (Taylor's Version),1989 (Taylor's Version)
Taylor Swift,Blank Space (Taylor's Version),1989 (Taylor's Version)
Peter Frampton,Show Me The Way,Frampton Comes Alive!
Peter Frampton,Do You Feel Like We Do,Frampton Comes Alive!
Michael Jackson,Billie Jean,Thriller
Michael Jackson,Thriller,Thriller
""".strip()


#################################################
# BEGIN: Don't edit this code                   #
#################################################
def read_song_db() -> list:
    """
    Reads CSV data containing a list of artist names and song titles
    in the format:

        artist,song,album

    Where each artist, song and title is separated by a comma, hence the type
    of file is CSV or Comma Separated Values.

    Returns:
        list (str): A list of strings containing artist, song title, and album separated by a comma
    """
    # Define a list to hold the CSV data
    data = []
    # Split a string containing End-of-Line chars (\n) into a list of lines
    rows = SAMPLE_CSV_DATA.splitlines()
    # Get the first line which includes the heading of each column, separated by commas
    # We won't use this data in this application
    headings = rows[0].split(',')

    # Get each row of data, skipping the first row which is headings
    for row in rows[1:]:
        data.append(row)

    return data


# Filename for song DB backup
SONG_DB_FILE = "song_db.json"


def backup_db(song_db: dict) -> None:
    """ Back up the song database to disk """
    with open(SONG_DB_FILE, "w") as file_handle:
        json.dump(song_db, file_handle)


def restore_db() -> dict:
    """ Restore the song database from disk """
    if os.path.exists(SONG_DB_FILE):
        with open(SONG_DB_FILE, "r") as file_handle:
            song_db = json.load(file_handle)
            return song_db
    else:
        print("No song database found, have you backed it up?")
#################################################
# END: Don't edit this code                     #
#################################################


def load_initial_db() -> dict:
    """
    Split each line of data to get artist, song and album and save the information in a database
    that is a dictionary.  You may structure the dictionary any way you choose, but based on the
    functions you will write, some dictionary structures may be more efficient.

    Returns:
        dict: Returns the sample song database as a dictionary
    """
    db = dict()
    # Load the initial song database
    for line in read_song_db():
        pass  # Remove this line and replace with your code

    return db


def find_artist_songs(artist: str, in_db: dict) -> list:
    """ Find all songs by an artist name

    Arguments:
        artist (str): The name of the artist to search for in the database
        in_db (dict): Song dictionary to search

    Returns:
        list (str): Returns a list of strings containing the string album/song names or an empty list if
        there are no songs by the artist
    """
    pass  # Replace this line with your code for this function


def find_songs_like(text: str, in_db: dict) -> list:
    """ Find all songs that include ``text`` as part of the song title.

    Arguments:
        text (str): The string to search for in song titles
        in_db (dict): Song dictionary to search

    Returns:
        list (str): A list containing the string artist/album/song for all of matching entries
        or an empty list if there are no songs by the artist
    """
    pass  # Replace this line with your code for this function


def help():
    """ Print the list of commands supported by the program. """
    pass  # Replace this line with your code for this function


# Setup program variables
# Set the flag to indicate when to stop
running = True

# Create a new database to hold the songs
song_database = load_initial_db()

# Show help before starting
help()

# Main program loop
while running:
    for db_key in song_database.keys():
        print("Key:", db_key, "Value:", song_database[db_key])
    running = False
