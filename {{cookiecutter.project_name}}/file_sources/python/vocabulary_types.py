from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class ControlledName(VocabularyType):
    defs = VocabularyTypeDef(
        code="CONTROLLED_NAME",
        description="""A controlled and well-defined name for the example object type//Ein kontrollierter und wohldefinierter Name für den Beispielobjekttyp""",
    )

    hello = VocabularyTerm(
        code="HELLO",
        label="Hello",
        description="""The word „Hello“ in the typical „Hello World“ initial program in any programming language//Das Wort „Hello“ im typischen „Hello World“-Startprogramm in jeder Programmiersprache""",
    )

    world = VocabularyTerm(
        code="WORLD",
        label="World",
        description="""The word „World“ in the typical „Hello World“ initial program in any programming language//Das Wort „World“ im typischen „Hello World“-Startprogramm in jeder Programmiersprache""",
    )
