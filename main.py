import bitcoin as btc


def generate_private_key(seed):
    private_key = btc.sha256(seed)
    return private_key


# 04 + x coordinate + y coordinates -> (multiplication of private key and generator)
def generate_public_key(private_key):
    public_key = btc.privkey_to_pubkey(private_key)
    return public_key


def get_address(public_key):
    address = btc.pubkey_to_address(public_key)
    return address


if __name__ == '__main__':
    # please ensure that the seed is a strong and safe random number!
    private_key = generate_private_key('PROVIDE_A_SECRET_AND_RANDOM_VALUE')

    public_key = generate_public_key(private_key)

    # please enter the PUBLIC key! Not the private key!
    address = get_address(public_key)

    print('private key (SECRET): ', private_key, '\n', 'public key: ', public_key, '\n', 'address: ', address)

