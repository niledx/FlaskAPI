from flask import Flask

app = Flask(__name__)

@app.route('/member', methods=['GET'])
def get_members():
    return 'This returns all members'


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    return 'This returns member by id {}'.format(member_id)


@app.route('/member', methods=['POST'])
def add_members():
    return 'This adds a new member'

@app.route('/member/<int:member_id>', methods=['PUT','PATCH'])
def edit_member(member_id):
    return 'This edits member with id {}'.format(member_id)

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'This deletes member with id {}'.format(member_id)


if __name__ == '__main__':
    app.run(debug=True)