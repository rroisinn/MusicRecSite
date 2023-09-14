DROP TABLE IF EXISTS music;

CREATE TABLE music 
(
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rec INTEGER,
    song TEXT,
    link TEXT
    
    
);

INSERT INTO music (name, rec, song, link)
VALUES
  ('Taylor Swift', NULL,NULL, NULL),
  ('Phoebe Bridgers', NULL,NULL, NULL),
  ('Olivia Rodrigo', NULL,NULL, NULL),
  ('Wallows', NULL,NULL, NULL),
  ('Ed Sheeran', NULL,NULL, NULL),
  ('Ariana Grande', NULL,NULL, NULL),
  ('Lorde', NULL,NULL, NULL),
  ('Harry Styles', NULL,NULL, NULL),
  ('Billie Eilish', NULL,NULL, NULL),
  ('Maisie Peters', 1,'Love Him I Dont', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO1EAce1?si=e10040e8e20c4900'),
  ('Gracie Abrams', 1,'I Miss you, Im Sorry', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO2Cuzya?si=094d63dfeebe4312'),
  ('Holly Humberstone', 1,'Scarlett', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO09APw6?si=8e67695455554974'),
  ('Alix Page', 2,'25', 'https://open.spotify.com/artist/7hp6PmppZj6iiolLVT4iEZ?si=u7RShGEzSg-aVFmuH4JlaQ'),
  ('Tommy Lefroy', 2,'Trashfire', 'https://open.spotify.com/artist/3vldh5Ceynytj6Iglw4haP?si=3Bs8K0diQhyECkDVIwFVZw'),
  ('Saint Street', 2,'Cheap Apple Cider', 'https://open.spotify.com/artist/3xxtBiChl6ziXmxgmbufgC?si=E2KAW_6rQxGFe9ha1R7Tjw'),
  ('Pom Pom Squad', 3,'Head Cheerleader', 'https://open.spotify.com/artist/1yhTALwId0bpL1U1XRT3Zs?si=VUkhq4mYS0WEJc_39Yul0g'),
  ('Maude Latour', 3,'Block Your Number', 'https://open.spotify.com/artist/3MNLhvqJkWsO6tcjY9ps62?si=Dbj1ZIFpSieqyKkymVznVQ'),
  ('Laura Elliot', 3,'Blue', 'https://open.spotify.com/artist/0YJEuTCD642Yp34CoiH0ox?si=0aaJ1KhDTnavT6uH423lvQ'),
  ('Lovejoy', 4,'Perfume', 'https://open.spotify.com/artist/33tFkBLsl6f8TjKkV0uF0C?si=7pgUfnIrTG2AqDQTzIzWXg'),
  ('THE JACKS', 4,'Slowly', 'https://open.spotify.com/artist/2MaOt31JjxLUV3E62dkbRw?si=8wxZNwHRSHidycpxf_4Rjg'),
  ('The Academic', 4,'Not Your Summer', 'https://open.spotify.com/artist/3VLf4DlBTN2ZRwygS3TNti?si=DxdHpzhwSC2CUtEzGno72A'),
  ('Alec Benjamin', 5,'Shadow of mine', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO3mWKYL?si=9aa3c70980a44294'),
  ('Thomas Headon', 5,'Clean me up', 'https://open.spotify.com/artist/0dn62y7ayEAxcIcMcBWXIE?si=GlFVlo12TTOef3siz-6gOQ'),
  ('Alexander 23', 5,'IDK you yet', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO3OC4Tf?si=ae38cc9fcb3c424a'),
  ('spill tab', 6,'PISTOLWHIP', 'https://open.spotify.com/artist/3qqkHeEhezlIaNj1vFYH2r?si=v025ZobsS_ufsvOjnN9__w'),
  ('MAY-A', 6,'Apricots', 'https://open.spotify.com/artist/5J8UACGRZtDb4WdOzo9YJN?si=tYC7reQaSy-uqqwBvOPWDw'),
  ('Sycco', 6,'Nicotine', 'https://open.spotify.com/artist/4meTRfbaVba24HXyBwbKJ0?si=Kd_5Sw9zQEqXSWVeE9LtFw'),
  ('dee holt', 7,'Olivia', 'https://open.spotify.com/artist/4PGmuxahHxpeLAGrR6ygKL?si=9jkrwLTrTuyMyQW0eT0xHg'),
  ('Wallice', 7,'Hey Michael', 'https://open.spotify.com/artist/6d6ts87Fxm1EdULf4CaLw4?si=enu8mDofTvOXPYJwILagBQ'),
  ('The Marias', 7,'Hush', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO1pweud?si=6940019c45384fab'),
  ('Ryan Woods', 8,'WALLS', 'https://open.spotify.com/artist/2Zgc1KUqd7A9wmQ7mQHuwY?si=tMcI7txGQE2VwCvT_hEeZA'),
  ('Max Leone', 8,'in case(theres a change of heart)', 'https://open.spotify.com/artist/4VrJDwgmhD1aIenZwn7JpE?si=bd1I6C5TQYau1zJzgt4IKg'),
  ('Cristain Leave', 8,'10 Steps', 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO1xuPBd?si=dd92b241cbb6457e'),
  ('Ella Jane', 9,'through the looking glass', 'https://open.spotify.com/artist/3gBjSrNsYzzbeo0nwsL21J?si=RfDUGtdCRLCwSbf5M3fMcA'),
  ('Jenna Doe', 9,'Pink Slips', 'https://open.spotify.com/artist/537KNo7PHzbkHiv5SGQ0eT?si=t-C5Es3wR9-8HzesRO9eWQ'),
  ('AUDREY NUNA', 9,'damn right', 'https://open.spotify.com/artist/0Wwji82sLA0Hcvtuak3omb?si=LhSN7aDUQy63YIL6BVDXWQ')
  ;

DROP TABLE IF EXISTS users;

CREATE TABLE users
( user_id  TEXT PRIMARY KEY,
password  TEXT NOT NULL);
  


DROP TABLE IF EXISTS mailinglist;

CREATE TABLE mailinglist
( id  INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email  TEXT NOT NULL);

SELECT *
FROM users

DROP TABLE IF EXISTS recommendations;

CREATE TABLE recommendations
( id  INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
rec  TEXT NOT NULL);