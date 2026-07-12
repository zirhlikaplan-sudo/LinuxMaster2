#!/bin/sh
GRADLE_OPTS=""
JAVACMD="java"
APP_HOME="$(cd "$(dirname "$0")" && pwd)"
exec "$JAVACMD" -jar "$APP_HOME/gradle/wrapper/gradle-wrapper.jar" "$@"
