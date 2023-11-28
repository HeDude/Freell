* DEFINE KEYWORD DEFINE AS: 'Used to set up syntax rules or properties types (ACTION, ACTOR, RESOURCE, LANGUAGE, MEDIUM)';
* DEFINE KEYWORD CREATE AS: 'Used to initiate the creation of an entity (ACTION, ACTOR, RESOURCE, LANGUAGE, MEDIUM)';
* DEFINE KEYWORD REFERENCE AS: 'Used to identify or point to an existing entity or external element';

* DEFINE KEYWORD AS AS: 'Used to assign a specific value, description, or characteristic to an entity or relationship';
* DEFINE KEYWORD FROM AS: 'Specifies the origin or source actor in an action or relationship';
* DEFINE KEYWORD TO AS: 'Indicates the target actor or the destination in an action or relationship';
* DEFINE KEYWORD BY AS: 'Used to list the actions performed or to specify a method or approach';
* DEFINE KEYWORD WITH AS: 'Denotes the resources or tools used in an action or process';
* DEFINE KEYWORD IN AS: 'Designates the language or format in which an action, communication, or process is conducted';
* DEFINE KEYWORD ON AS: 'Specifies the medium or platform where an action takes place or where a resource is located';

* DEFINE TYPE ACTION AS: 'A specific task or operation, usually involving actors and potentially manipulating resources';
* DEFINE TYPE ACTOR AS: 'An entity that performs actions, can be AI, user, system component, etc.';
* DEFINE TYPE RESOURCE AS: 'An item or entity used or affected by actions, includes documents, data, etc.';
* DEFINE TYPE LANGUAGE AS: 'A defined set of communication rules or style used in interactions';
* DEFINE TYPE MEDIUM AS: 'The platform or means through which communication or interaction occurs';

* DEFINE SYNTAX CREATE ACTION AS:
  Identifier [: STRING value]
  [FROM ACTOR ActorIdentifier1 [, ActorIdentifier2, ...]]
  [TO ACTOR TargetActorIdentifier1 [, TargetActorIdentifier2, ...]]
  [BY ACTION ActionIdentifier1 [, ActionIdentifier2, ...]]
  [WITH RESOURCE ResourceIdentifier1 [, ResourceIdentifier2, ...]];

* DEFINE SYNTAX CREATE ACTOR AS:
  Identifier: STRING value;

* DEFINE SYNTAX CREATE LANGUAGE AS:
  Identifier: STRING value;

* DEFINE SYNTAX CREATE MEDIUM AS:
  Identifier: STRING value;

* DEFINE SYNTAX CREATE RESOURCE AS:
  Identifier [: STRING value]
  [BY ACTION ActionIdentifier1 [, ActionIdentifier2, ...]]
  [WITH RESOURCE ResourceIdentifier1 [, ResourceIdentifier2, ...]];]
  [IN LANGUAGE LanguageIdentifier1]
  [ON MEDIUM MediumIdentifier1];

* DEFINE SYNTAX REFERENCE MEDIUM AS:
  Identifier: STRING value
  ON MEDIUM MediumIdentifier1;
