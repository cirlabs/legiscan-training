# Reveal Reporting Network Training: Structured Legislative Data with LegiScan

Read : [Big Lie Proponents Are Creating Harsh Criminal Penalties for Elections Activity](https://revealnews.org/article/election-crime-legislation-voter-suppression/)

Listen: [The Ballot Boogeymen
](https://revealnews.org/podcast/the-ballot-boogeymen/)

Explore: [Search for the Crime Bills That Target Voting and Elections in Your State](https://revealnews.org/article/search-for-the-crime-bills-that-target-voting-and-elections-in-your-state/)

***

Note: Until the training, this repo is:

![](01_inputs/documentation/construction.gif)

This repository contains Python scripts that interface with the LegiScan API to retrieve, collate and analyze structured data on legislation at both the federal and state level.

You'll be able to examine the history of a specific bill, analyze legislative action on a specific issue over a decade’s time[^1] or simply create an organized system for tracking the next session.
## Requirements
### Python
- [ ] Version 3.8 or later

#### Packages
See [Installation](#installation)

### Legiscan
- [ ] An [account](https://legiscan.com/user/register) (free)
  ![Sceenshot of the LegiScan account creation page, depicting radio buttons under the form item labeled "Account Type," where the first item ("OneVote - Free public service [..]") is selected](01_inputs/documentation/legiscan_account_creation.png "LegiScan registration page")
- [ ] An [API key](https://legiscan.com/legiscan) (only possible once you've verified the email address under which you registered)
## Setup
### Virtual Environment
* I've only used pyenv for the last few years, but you should be able to use conda, etc. if that's what you're comfortable with!

  #### pyenv

    ```
    pyenv virtualenv 3.10.4 great_virtualenv_name
    ```

### Installation

```bash
pip install -r requirements.txt
```
## Contributors

* [@meli-lewis](https://github.com/meli-lewis)

## Contact

If you want to contact me you can reach me at the email address listed in my profile, or through one of the methods on my [Reveal staff page](https://revealnews.org/author/melissa-lewis/).

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>, which is -- as of  [2022](https://web.archive.org/web/20221117230734/https://legiscan.com/legiscan) -- specified by the LegiScan API.

[^1]: See https://legiscan.com/legiscan-states for jurisdiction-specific availability.