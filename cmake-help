#!/usr/bin/env python

import sys, cmd
from subprocess import Popen, PIPE

#--help-command-list [file]  = List available listfile commands and exit.
#--help-module-list [file]   = List available modules and exit.
#--help-property-list [file] = List available properties and exit.
#--help-variable-list [file] = List documented variables and exit.
intro ="""
Welcome to the interactive CMake Help system

To view the documentation for a specific CMake element
use on of the following commands:

    command   -  Print help for a single command'
    module    -  Print help for a single module
    property  -  Print help for a single property
    variable  -  Print help for a single variable

To get a list of available elments use the Tab completetion:

    [CMake Help] command fi<TAB>

"""

class CMakeHelp(cmd.Cmd):
    def __init__(self):
        """
        keywords - keyword cache for CMake elements (commands, modules, etc..)
        """
        cmd.Cmd.__init__(self)
        self.prompt = "[CMake Help] "
        self.keywords = {}
        self.intro = intro
        
        self.cmake_cmd= 'cmake'
        self.pager_cmd= 'less'

    def display_cmake_help(self, _type, keyword):
        """ Executes CMake help in a pager

            _type   - Element type
            keyword - Element name
        """
        cmd_args = (self.cmake_cmd, _type, keyword, self.pager_cmd)
        Popen('%s --help-%s %s | %s' % cmd_args, shell=True).communicate()

    def get_cmake_keywords(self, _type):
        """ Gets a list of available element keywords for the given CMake type and cachces them.

            _type - CMake element type
        """
        if not _type in self.keywords:
            cmd_args = (self.cmake_cmd, _type)
            self.keywords[_type]= Popen('%s --help-%s-list' % cmd_args, shell=True, stdout=PIPE).communicate()[0].splitlines()
        return self.keywords[_type]

    def get_cmake_completions(self, _type, text):
        """ Returns a list of available CMake element keywords. 

            _type - CMake element type
            text  - Partial element name
        """
        completions = keywords = self.get_cmake_keywords(_type)
        if not text:
            completions = keywords
        else:
            completions = [ keyword
                            for keyword in keywords
                            if keyword.startswith(text)
                          ]
        return completions

    #=========================================================#
    #  Command command                                        #
    #=========================================================#
    def do_command(self, arg):
        """Display CMake command help"""
        self.display_cmake_help('command', arg)

    def help_command(self):
        """Display command help"""
        print
        print 'Print help for a single command'
        print

    def complete_command(self, text, line, begidx, endidx):
        """Retrun available CMake commands"""
        return self.get_cmake_completions('command', text)
    
    do_c = do_command
    help_c = help_command
    complete_c = complete_command


    #=========================================================#
    #  Module command                                         #
    #=========================================================#
    def do_module(self, arg):
        """Display CMake moudle help"""
        self.display_cmake_help('module', arg)

    def help_module(self):
        """Display module help"""
        print
        print 'Print help for a single module'
        print

    def complete_module(self, text, line, begidx, endidx):
        """Retrun available CMake modules"""
        return self.get_cmake_completions('module', text)
    
    do_m = do_module
    help_m = help_module
    complete_m = complete_module


    #=========================================================#
    #  Property command                                       #
    #=========================================================#
    def do_property(self, arg):
        """Display CMake property help"""
        self.display_cmake_help('property', arg)

    def help_property(self):
        """Display property help"""
        print
        print 'Print help for a single property'
        print

    def complete_property(self, text, line, begidx, endidx):
        """Retrun available CMake properties"""
        return self.get_cmake_completions('property', text)
    
    do_p = do_property
    help_p = help_property
    complete_p = complete_property


    #=========================================================#
    #  Variable command                                       #
    #=========================================================#
    def do_variable(self, arg):
        """Display CMake variable help"""
        self.display_cmake_help('variable', arg)

    def help_variable(self):
        """Display property help"""
        print
        print 'Print help for a single variable'
        print

    def complete_variable(self, text, line, begidx, endidx):
        """Retrun available CMake variables"""
        return self.get_cmake_completions('variable', text)
    
    do_v = do_variable
    help_v = help_variable
    complete_v = complete_variable




    #=========================================================#
    #  Quit command                                           #
    #=========================================================#
    def do_quit(self, arg):
        """Terminates CMake Interactive Help system"""
        print
        sys.exit(1)

    def help_quit(self):
        """Quit help message"""
        print 'Terminates CMake Interactive Help System'

    do_EOF = do_quit
    help_EOF = help_quit


def main():
    """Main entry point"""
    try:
        cmh = CMakeHelp()
        cmh.cmdloop()
    except KeyboardInterrupt:
        # Catch Ctrl-c and exit gracefully
        pass
    print

if __name__ == '__main__':
    main()
