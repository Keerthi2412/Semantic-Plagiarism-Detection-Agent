from flask import Flask, render_template, request, jsonify

from document_processor import (
    extract_text,
    split_into_sections
)

from analyzer import analyze


app = Flask(__name__)


# -----------------------------
# HOME PAGE
# -----------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -----------------------------
# ANALYSIS API
# -----------------------------

@app.route("/analyze", methods=["POST"])
def run_analysis():

    submitted_file = request.files.get(
        "submitted"
    )

    reference_file = request.files.get(
        "reference"
    )


    # Check files
    if not submitted_file or not reference_file:

        return jsonify({

            "error":
            "Please upload both the submitted and reference documents."

        }), 400


    try:

        # Extract text
        submitted_text = extract_text(
            submitted_file
        )

        reference_text = extract_text(
            reference_file
        )


        # Split into sections
        submitted_sections = split_into_sections(
            submitted_text
        )

        reference_sections = split_into_sections(
            reference_text
        )


        # Check extracted content
        if not submitted_sections:

            return jsonify({

                "error":
                "Could not extract readable text from the submitted document."

            }), 400


        if not reference_sections:

            return jsonify({

                "error":
                "Could not extract readable text from the reference document."

            }), 400


        # Run semantic analysis
        result = analyze(

            submitted_sections,

            reference_sections

        )


        return jsonify(result)


    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# -----------------------------
# START APPLICATION
# -----------------------------

if __name__ == "__main__":

    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )
