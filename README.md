# CYB333-Final-Project

Most password managers create stronger passwords for you, but they are not easy to remember. The easier passwords to remember are usually things like your birthday or things that compromise security for convenience. This is my best attempt to combine password memorability with strength, and compare it to a strong password guideline.

https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-strong-passwords

According to this CISA guideline, here are the requirements that relate the closest to this project's goal:

*Long: At least 16 characters long (more is better)*
*Random: A mix of upper/lowercase letters, numbers and symbols or a passphrase of 5–7 unrelated words*

## How it works:

This software takes input from the passwordReplacement.txt, and searches for the first character of each line in your passwords, such as "I" as an example. It goes through each word in input.txt, looking for this letter. Finally, it would switch the character out for "!" or "L", and places them in output.txt.

This allows for scalable strengthening of passwords with a configurable character replacement to fit your I.T guidelines. Given the extended time that I had, this tool isn't able to extend the given passwords' length with numbers, despite my quick attempts.




