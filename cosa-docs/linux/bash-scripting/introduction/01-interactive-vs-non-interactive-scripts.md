# Interactive and Non-Interactive Scripts

Interactive scripts have a more complex control flow because it depends on user input. Non-interactive scripts follow a linear or branched control flow determined entirely by the script's code.

Interactive scripting is where there is user presence and inputs are dealt lively. 

Another practical implication of this can be seen using the following example as given below.

```bash 
# live script
> echo "this is a random variable ${PS1}"
this is a random variable $

# non-interactive script
> bash test.sh # containing same echo script as above
This is a random variable 
```

Interactive and Non-interactive shell scripting is concept that is used and should be understood. Interactive shell scripting is interacting with the shell directly using commands in the command line, and another is Non-Interactive which is interacting with the shell using some command inside the files to achieve some automation, which inturns invoke bash, which is better known as [*Shell Scripting using Bash*](02-bash-vs-shell-scripting.md).


