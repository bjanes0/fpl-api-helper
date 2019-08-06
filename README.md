# fpl-api-navigator
A fantasy premier league library with python applications to use the API and libraries of parsed information

## The API Structure
The FPL API has changed for the 19/20 season and is now located at https://fantasy.premierleague.com/api/. In addition, a change on August 1st 2019 impacted some of the previously working parts of the API, now making them limited or nonexistent. 

Currently working with no authentication:
* /bootstrap-static*
* /fixtures
* /regions
* /entry/entry-id

Working but **requires authentication**:
* /my-team/logged-in-team-id
* /leagues-classic/league-id
* /leagues-classic/league-id/standings
* /leagues-h2h/league-id/
* /leagues-h2h/league-id/standings

Exists but no data returned:
* /transfers (may not exist in pre-season)

Previously accessible but no longer in use:
* /events
* /leagues-entered/logged-in-team-id
* /teams 

## Notes
The elements of bootstrap-static include
* events
* game_settings
* phases
* teams
* total_players
* elements
* element_stats
* element_types

