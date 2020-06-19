#!/usr/bin/env python

import argparse
import re
import os
import errno

def pageContent(className):
    return '''import 'package:flutter/material.dart';

class ''' + className + ''' extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
'''

def blocContent(blocName, stateName, eventName, statePath, eventPath):
    return '''import 'package:flutter_bloc/flutter_bloc.dart';

part ''' + "'" + eventPath + "'" + ''';
part ''' + "'" + statePath + "'" + ''';

class ''' + blocName + ''' extends Bloc<''' + eventName + ''', ''' + stateName + '''> {
  @override
  ''' + stateName + ''' get initialState => throw UnimplementedError();

  @override
  Stream<''' + stateName + '''> mapEventToState(''' + eventName + ''' event) {
    throw UnimplementedError();
  }
}
'''

def stateContent(className, blocPath):
    return '''part of ''' + "'" + blocPath + "'" + ''';

abstract class ''' + className + ''' { }
'''

def eventContent(className, blocPath):
    return '''part of ''' + "'" + blocPath + "'" + ''';

abstract class ''' + className + ''' { }
'''

extension = '.dart'
page = "Page"
bloc = "Bloc"
state = "State"
event = "Event"

def getClassName(contextName, ending):
    parts = contextName.split('_')
    parts = [part.title() for part in parts]
    return ''.join(parts) + ending

def getFileName(contextName, ending):
    return contextName + '_' + ending.lower() + extension

def createDirIfNeeded(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

parser = argparse.ArgumentParser(description='Generate flutter page folder with bloc.')
parser.add_argument('-n', '--name', 
                    help='Provide contextual name of your new page, for [-n departure_list] you will get departure_list_page.dart with class name DepartureListPage', 
                    required=True)

parsedArgs = parser.parse_args()

contextName = parsedArgs.name.lower()

pageFileName = getFileName(contextName, page)
blocFileName = getFileName(contextName, bloc)
stateFileName = getFileName(contextName, state)
eventFileName = getFileName(contextName, event)

pageClassName = getClassName(contextName, page)
blocClassName = getClassName(contextName, bloc)
stateClassName = getClassName(contextName, state)
eventClassName = getClassName(contextName, event)

newPagePath = './lib/presentation/' + contextName + '/'

pageFilePath = newPagePath + pageFileName
blocFilePath = newPagePath + blocFileName
stateFilePath = newPagePath + stateFileName
eventFilePath = newPagePath + eventFileName

createDirIfNeeded(pageFilePath)

with open(pageFilePath, 'w') as file:
    file.write(pageContent(pageClassName))

with open(blocFilePath, 'w') as file:
    file.write(blocContent(blocClassName, stateClassName, eventClassName, stateFileName, eventFileName))

with open(stateFilePath, 'w') as file:
    file.write(stateContent(stateClassName, blocFileName))

with open(eventFilePath, 'w') as file:
    file.write(eventContent(eventClassName, blocFileName))