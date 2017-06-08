# alfresco_papers

Some Alfresco related papers I wrote while Francis K was our manager. 


Those papers are written in LaTeX. To generate a pdf output, it should be as simple as changing directory to the paper's directory, look for a file ending with '.tex' e.g file.tex and type:

```shell
pdflatex file.tex
```

## capacity_planning 	

Capacity planning paper:
How big you would expect your indexes to be depending on the content size. We are looking here for the worst case scenario to get upper bounds.

## kerberos_join_network 	

What does mean for a computer to "join a network"?
This paper explains it means writing some records in the LDAP directory (AD).

## kerberos_linux 	

Alfresco kerberos with linux KDC.
Alfresco kerberos authentication is only supported when the KDC is Active Directory. However, it does work also with a Linux KDC (but you need to get your hands dirty).

## websphere_fastinstall 	

Websphere fast install using the jython scripting language of WAS.
Or how to create a test websphere setup in one command.

