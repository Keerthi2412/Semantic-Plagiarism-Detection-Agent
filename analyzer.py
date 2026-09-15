from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load pre-trained semantic embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def analyze(submitted_sections, reference_sections):

    # Generate semantic embeddings
    submitted_embeddings = model.encode(
        submitted_sections
    )

    reference_embeddings = model.encode(
        reference_sections
    )


    # Calculate similarity between all sections
    similarity_matrix = cosine_similarity(
        submitted_embeddings,
        reference_embeddings
    )


    matches = []


    # Find best reference match for every submitted section
    for i, similarities in enumerate(similarity_matrix):

        best_index = similarities.argmax()

        similarity_score = (
            similarities[best_index] * 100
        )


        # Only show potentially significant matches
        if similarity_score >= 50:

            matches.append({

                "submitted_section":
                    i + 1,

                "reference_section":
                    best_index + 1,

                "similarity":
                    round(similarity_score, 2),

                "submitted_text":
                    submitted_sections[i],

                "reference_text":
                    reference_sections[best_index]

            })


    # Calculate overall semantic similarity
    best_matches = similarity_matrix.max(axis=1)

    overall_similarity = (
        best_matches.mean() * 100
    )


    # Determine plagiarism risk
    if overall_similarity >= 75:

        risk = "HIGH"

    elif overall_similarity >= 50:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    return {

        "overall_similarity":
            round(float(overall_similarity), 2),

        "risk":
            risk,

        "matches":
            matches,

        "submitted_sections":
            len(submitted_sections),

        "reference_sections":
            len(reference_sections)

    }
