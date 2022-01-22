# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of recent local congressional elections.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- software: Python 3.9.7, Visual Studio Code, 1.63.2

## Summary
The analysis of the election show the following:
- There were 396,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.  
  - Diana DeGette received 73.8% of the vote and 272,892 votes.  
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.         
- The winner of the election was:
  - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 votes
![Election Results](https://user-images.githubusercontent.com/95668609/150623328-11c04caf-613c-4ba0-8f1d-0d9627b97e8f.png)

## Challenge Overview
# Overview of Election Audit
The challenge was trying to obtain some additional data that was requested by the elction commision in order to get the scope of the participation by county.
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout 
Overview of Election Audit

# Election-Audit Results
1. How many votes were cast in this congressional election?
- There were 396,711 votes cast in this congressional election.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Jefferson: 10.5% (38855)
- Denver: 82.8% (306055)
- Arapahoe: 6.7% (24801)
3. Which county had the largest number of votes?
- Denver had the largest number of votes
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%
![Election Results - Challenge](https://user-images.githubusercontent.com/95668609/150623387-154a0e34-7155-47d6-ad7f-545780b66dcb.png)

## Challenge Summary
# Election-Audit Summary
Bosed on how this scritp was created we can ensure it can be use in the future for any elctions audits that the election commissions needs to perform.
The current audit scritp can be modify in oder to obtain same results for any election, this is possible by the usage of variables that can be rename.
- Example:
    a) If we need to audit any other state, you would have to updade the file containing the election results and confirm that the colums are in the same order. Since the county and candidates are set variables the outcome will be the same depending on the new information prvided and considerng the new date this script will provide the same result that has been provided when auditing this election.
    b) Since the formulas that will need to be use in future elctions are the sames, we will need only to modify the new variables that need to be used and will result in the calculations already stablished and proven in this analysis.
In summary the usage od this script will be possible for future elcetion audit by using the same structure and updating some variables by renaming them and we will otain the same results.
