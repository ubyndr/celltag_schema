

CREATE TABLE "AutomatedCellTypeAnnotationMetadata" (
	algorithm TEXT, 
	algorithm_reference TEXT, 
	reference_data TEXT, 
	PRIMARY KEY (algorithm, algorithm_reference, reference_data)
);

CREATE TABLE "Container" (
	meta TEXT, 
	PRIMARY KEY (meta)
);

CREATE TABLE "CxGMetaSchema" (
	field_name TEXT NOT NULL, 
	field_type VARCHAR(24) NOT NULL, 
	field_scope VARCHAR(5), 
	field_relationship TEXT, 
	manual_annotation_metadata TEXT, 
	automated_cell_type_annotation_metadata TEXT, 
	PRIMARY KEY (field_name, field_type, field_scope, field_relationship, manual_annotation_metadata, automated_cell_type_annotation_metadata)
);

CREATE TABLE "FieldRelationship" (
	relation VARCHAR(12) NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (relation, object)
);

CREATE TABLE "ManualAnnotationMetadata" (
	author TEXT, 
	supporting_publication TEXT, 
	evidence_comment TEXT, 
	marker_evidence TEXT, 
	PRIMARY KEY (author, supporting_publication, evidence_comment, marker_evidence)
);
