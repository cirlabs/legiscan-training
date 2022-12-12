# Inputs

## `bills/`

Except where noted, the following directly replicates the `bill` data dictionary on p.33 of the LegiScan API v.1.85 manual (Revision 20220108).<sup>[archive link](https://web.archive.org/web/20221212054056/https://legiscan.com/misc/LegiScan_API_User_Manual.pdf)</sup>

`*`: Documented in the API manual as "array," but returned as a JSON object, which Python deserializes to a dictionary.

| Field                         | Type | Description                                                                     |
|-------------------------------|-----------|---------------------------------------------------------------------------------|
| bill_id                       | integer   | Internal bill id                                                                |
| change_hash                   | string    | MD5 hash of bill status meta-data to aid change detection in Pull               |
| last_push                     | datetime  | Timestamp of last successful push (Push Only)                                   |
| session_id                    | integer   | Internal session id                                                             |
| session                     | dict*   | Array of session information                                                    |
| &emsp;session_id              | integer   | Internal session id                                                             |
| &emsp;year_start              | integer   | Starting year of the session                                                    |
| &emsp;year_end                | integer   | Ending year of the session                                                      |
| &emsp;prefile                 | integer   | Flag for session being in prefile (0, 1)                                        |
| &emsp;sine_die                | integer   | Flag for session being adjourned sine die (0, 1)                                |
| &emsp;prior                   | integer   | Flag for session being archived out of production updates (0, 1)                |
| &emsp;special                 | integer   | Flag for being a special session (0, 1)                                         |
| &emsp;session_name            | string    | State specific session name                                                     |
| &emsp;session_title           | string    | Normalized session title with year(s) and Regular/Special Session               |
| url                           | string    | LegiScan URL                                                                    |
| state_link                    | string    | State URL                                                                       |
| completed                     | integer   | DEPRECATED DO NOT USE                                                           |
| status                        | integer   | Internal progress id for Intro, Engross, Enroll, Pass, Veto                     |
| status_date                   | date      | Date of status action                                                           |
| progress                 | array     | History array converted to significant progress steps to calculate status field |
| &emsp;step                | dict*     | Individual progress records                                                     |
| &emsp;&emsp;date              | date      | Date of event                                                                   |
| &emsp;&emsp;event             | integer   | Internal event type id matching the history action                              |
| state                         | string    | State abbreviation                                                              |
| state_id                      | integer   | Internal state id                                                               |
| bill_number                   | string    | Bill number                                                                     |
| bill_type                     | string    | Type of instrument text                                                         |
| bill_type_id                  | integer   | Internal bill type id                                                           |
| body                          | string    | Originating body text                                                           |
| body_id                       | integer   | Internal body id                                                                |
| current_body                  | string    | Current body text                                                               |
| current_body_id               | integer   | Internal body id                                                                |
| title                         | string    | Title                                                                           |
| description                   | string    | Description                                                                     |
| pending_committee_id          | integer   | Internal committee id                                                           |
| committee                 | array     | Array of committee info if currently pending                                    |
| &emsp;committee_id            | integer   | Internal committee id                                                           |
| &emsp;chamber                 | string    | Chamber of committee                                                            |
| &emsp;chamber_id              | integer   | Internal body id                                                                |
| &emsp;name                    | string    | Name of committee                                                               |
| referrals               | array     | Array of history steps                                                          |
| &emsp;referral             | array     | Individual history step                                                         |
| &emsp;&emsp;date              | date      | Date of referral                                                                |
| &emsp;&emsp;committee_id      | integer   | Internal committee id                                                           |
| &emsp;&emsp;chamber           | string    | Chamber of committee                                                            |
| &emsp;&emsp;chamber_id        | integer   | Internal body id                                                                |
| &emsp;&emsp;committee_name    | string    | Name of committee                                                               |
| history                 | array     | Array of history steps                                                          |
| &emsp;step                 | array     | Individual history step                                                         |
| &emsp;&emsp;date              | date      | Date of action                                                                  |
| &emsp;&emsp;action            | string    | Action step text                                                                |
| &emsp;&emsp;chamber           | string    | Chamber taking action                                                           |
| &emsp;&emsp;chamber_id        | integer   | Internal body id                                                                |
| &emsp;&emsp;importance        | boolean   | Flag for "major" steps, i.e., matches a progress condition (0, 1)               |
| sponsors                | array     | Array of sponsors                                                               |
| &emsp;sponsor              | dict*    | Individual sponsor record                                                       |
| &emsp;&emsp;people_id         | integer   | Internal people id                                                              |
| &emsp;&emsp;person_hash       | string    | Hash of the personal details to aid change detection                            |
| &emsp;&emsp;party_id          | integer   | Internal party id                                                               |
| &emsp;&emsp;party             | string    | Party text                                                                      |
| &emsp;&emsp;role_id           | integer   | Internal role id                                                                |
| &emsp;&emsp;role              | string    | Role text                                                                       |
| &emsp;&emsp;name              | string    | Full name                                                                       |
| &emsp;&emsp;first_name        | string    | First name                                                                      |
| &emsp;&emsp;middle_name       | string    | Middle name                                                                     |
| &emsp;&emsp;last_name         | string    | Last name                                                                       |
| &emsp;&emsp;suffix            | string    | Suffix                                                                          |
| &emsp;&emsp;district          | string    | Legislative district                                                            |
| &emsp;&emsp;ftm_eid           | integer   | FollowTheMoney.org EID                                                          |
| &emsp;&emsp;votesmart_id      | integer   | VoteSmart.org ID                                                                |
| &emsp;&emsp;opensecrets_id    | string    | OpenSecrets.org ID (Congress Only)                                              |
| &emsp;&emsp;knowwho_pid       | integer   | KnowWho.com PID                                                                 |
| &emsp;&emsp;ballotpedia       | string    | Ballotpedia.org Name                                                            |
| &emsp;&emsp;sponsor_type_id   | integer   | Internal sponsor type id (primary, co, joint)                                   |
| &emsp;&emsp;sponsor_order     | integer   | Index of order in sponsorship list                                              |
| &emsp;&emsp;committee_sponsor | boolean   | Committee sponsor flag (0, 1)                                                   |
| &emsp;&emsp;committee_id      | integer   | Internal committee id (if committee_sponsor)                                    |
| sasts                   | array     | Array of same as/similar to relations                                           |
| &emsp;sast                 | array     | Individual SA/ST record                                                         |
| &emsp;&emsp;type_id           | integer   | Internal sast id                                                                |
| &emsp;&emsp;type              | string    | Relationship text                                                               |
| &emsp;&emsp;sast_bill_number  | string    | Related bill number                                                             |
| &emsp;&emsp;sast_bill_id      | integer   | Internal bill id                                                                |
| subjects                | array     | Array of subjects                                                               |
| &emsp;subject              | array     | Individual subject record                                                       |
| &emsp;&emsp;subject_id        | integer   | Internal subject id                                                             |
| &emsp;&emsp;subject_name      | string    | Subject name                                                                    |
| texts                   | array     | Array of text drafts                                                            |
| &emsp;text                 | array     | Individual text record                                                          |
| &emsp;&emsp;doc_id            | integer   | Internal document id                                                            |
| &emsp;&emsp;date              | date      | Date of text if (available)                                                     |
| &emsp;&emsp;type              | string    | Type of draft text (introduced, amended, enrolled, comm sub, etc.)              |
| &emsp;&emsp;type_id           | integer   | Internal bill text type id                                                      |
| &emsp;&emsp;mime              | string    | MIME type of document                                                           |
| &emsp;&emsp;mime_id           | integer   | Internal mime type id                                                           |
| &emsp;&emsp;url               | string    | LegiScan URL                                                                    |
| &emsp;&emsp;state_link        | string    | State URL                                                                       |
| &emsp;&emsp;text_size         | integer   | Size in bytes of the decoded BASE64 document (add 33% for base64)               |
| &emsp;&emsp;text_hash         | string    | MD5 hash of the decoded BASE64 document                                         |
| votes                   | array     | Array of related roll calls                                                     |
| &emsp;vote                 | array     | Individual roll call record                                                     |
| &emsp;&emsp;roll_call_id      | integer   | Internal roll call id                                                           |
| &emsp;&emsp;date              | date      | vote date if available                                                          |
| &emsp;&emsp;desc              | string    | Roll call description                                                           |
| &emsp;&emsp;yea               | integer   | Count of yeas                                                                   |
| &emsp;&emsp;nay               | integer   | Count of nays                                                                   |
| &emsp;&emsp;nv                | integer   | Count of not voting                                                             |
| &emsp;&emsp;absent            | integer   | Count of absent                                                                 |
| &emsp;&emsp;total             | integer   | Total number of votes                                                           |
| &emsp;&emsp;passed            | boolean   | Passed flag (0, 1)                                                              |
| &emsp;&emsp;chamber           | string    | Origin chamber of vote                                                          |
| &emsp;&emsp;chamber_id        | integer   | Internal body id                                                                |
| &emsp;&emsp;url               | string    | LegiScan URL                                                                    |
| &emsp;&emsp;state_link        | string    | State URL                                                                       |
| amendments              | array     | Array of amendment documents                                                    |
| &emsp;amendment            | array     | Individual amendment record                                                     |
| &emsp;&emsp;amendment_id      | integer   | Internal amendment id                                                           |
| &emsp;&emsp;adopted           | boolean   | Flag for adoption (0, 1)                                                        |
| &emsp;&emsp;chamber           | string    | Origin chamber of amendment                                                     |
| &emsp;&emsp;chamber_id        | integer   | Internal body id                                                                |
| &emsp;&emsp;date              | string    | Amendment date (if available)                                                   |
| &emsp;&emsp;title             | string    | Amendment Title                                                                 |
| &emsp;&emsp;description       | string    | Amendment Description                                                           |
| &emsp;&emsp;mime              | string    | MIME type of document                                                           |
| &emsp;&emsp;mime_id           | integer   | Internal mime type id                                                           |
| &emsp;&emsp;url               | string    | LegiScan URL                                                                    |
| &emsp;&emsp;state_link        | string    | State URL                                                                       |
| &emsp;&emsp;amendment_size    | integer   | Size in bytes of the decoded BASE64 document (add 33% for base64)               |
| &emsp;&emsp;amendment_hash    | string    | MD5 hash of the decoded BASE64 document                                         |
| supplements             | array     | Array of supplemental documents                                                 |
| &emsp;supplement           | array     | Individual supplement record                                                    |
| &emsp;&emsp;supplement_id     | integer   | Internal supplement id                                                          |
| &emsp;&emsp;date              | date      | Supplement date (if available)                                                  |
| &emsp;&emsp;type_id           | integer   | Internal supplement type id                                                     |
| &emsp;&emsp;type              | string    | Supplement type text                                                            |
| &emsp;&emsp;title             | string    | Supplement title                                                                |
| &emsp;&emsp;description       | string    | Supplement description                                                          |
| &emsp;&emsp;mime              | string    | MIME type of document                                                           |
| &emsp;&emsp;mime_id           | integer   | Internal mime type id                                                           |
| &emsp;&emsp;url               | string    | LegiScan URL                                                                    |
| &emsp;&emsp;state_link        | string    | State URL                                                                       |
| &emsp;&emsp;supplement_size   | integer   | Size in bytes of the decoded BASE64 document (add 33% for base64)               |
| &emsp;&emsp;supplement_hash   | string    | MD5 hash of the decoded BASE64 document                                         |
| calendar                | array     | Array of events / hearings                                                      |
| &emsp;event                | array     | Individual event record                                                         |
| &emsp;&emsp;type_id           | integer   | Internal event type id                                                          |
| &emsp;&emsp;type              | string    | Event type text                                                                 |
| &emsp;&emsp;date              | date      | Event date                                                                      |
| &emsp;&emsp;time              | time      | Event time (if available)                                                       |
| &emsp;&emsp;location          | string    | Event location (if available)                                                   |
| &emsp;&emsp;description       | string    | Event description                                                               |

## `legiscan_static_lookup_tables/`

- `sast_type.csv`
- `supplement_type.csv`
- `sponsor_type.csv`
- `status.csv`
- `text_type.csv`
- `mime_type.csv`
- `state.csv`
- `event_type.csv`
- `party.csv`
- `body.csv`
- `role.csv`
- `reason.csv`
- `progress.csv`
- `vote.csv`
- `bill_type.csv`