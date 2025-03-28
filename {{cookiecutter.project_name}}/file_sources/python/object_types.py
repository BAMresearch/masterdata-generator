from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class ExampleObjectType(ObjectType):
    defs = ObjectTypeDef(
        code="EXAMPLE_OBJECT_TYPE",
        description="""
        An example to illustrate how to define an Object Type and its attributes//Ein Beispiel zur Veranschaulichung der Definition eines Objekttyps und seiner Attribute
        """,
        iri="http://purl.obolibrary.org/bam-masterdata/ExampleObjectType:0.0.0",
        generated_code_prefix="EXA_OBJ_TYP",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    # see `vocabulary_types.py` for the definition of this CONTROLLEDVOCABULARY
    controlled_name = PropertyTypeAssignment(
        code="CONTROLLED_NAME",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Controlled Name",
        description="""A controlled and well-defined name for the example object type//Ein kontrollierter und wohldefinierter Name für den Beispielobjekttyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )
