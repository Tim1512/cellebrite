from flask import Flask, request, jsonify
import utils 
import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

app = Flask(__name__)

@app.route("/api/v1/mors", methods=["GET"])
def get_my_ip():
    mors = utils.encrypt(message=request.remote_addr, mors_code_dict=MORSE_CODE_DICT)

    return jsonify({'ip_translate_to_mors': mors}), 200

if __name__ == '__main__':
    args = utils.parse_args()
    if not args.port:
        print("ERROR: Please enter app port with --port flag")
        sys.exit(1)
    else:
        app.run(host='0.0.0.0', debug=True, port=args.port)
