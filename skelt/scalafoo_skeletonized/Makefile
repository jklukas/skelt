export SERVICE := ${name}
DEPLOY = $(SERVICE)-service/target/$(SERVICE)-service

default: build
build: $(DEPLOY)

$(DEPLOY):
	MAVEN_OPTS="-XX:MaxPermSize=128m -Xmx1024m" $(MVN) -DforkMode=never clean deploy

test:
	$(MVN) test
