"""
Example evolution of NoKnow ZK Proof implementation
"""
from getpass import getpass
from noknow.core import ZK, ZKSignature, ZKParameters, ZKData, ZKProof
from queue import Queue
from threading import Thread

  

def main():
    
    # Set up test users
    usr1_credentials = "user1:secret1"
    usr2_credentials = "user2:secret2"

    # Set up server component
    server_password = "SecretServerPassword"
    server_zk = ZK.new(curve_name="secp384r1", hash_alg="sha3_512")
    server_signature: ZKSignature = server_zk.create_signature("SecureServerPassword")

    # Set up client component
    client_zk = ZK.new(curve_name="secp256k1", hash_alg="sha3_512")

    ### 1. Completeness: Verify ZKP without sending credentials ###

    # Create signature and send to server
    signature = client_zk.create_signature(usr1_credentials)

    # Load the received signature from the Client
    sig = signature.dump()
    client_signature = ZKSignature.load(sig)
    client_zk = ZK(client_signature.params)

    # Create a signed token and send to the client
    token = server_zk.sign("SecureServerPassword", client_zk.token())
    token = token.dump(separator=":")

    # Create a proof that signs the provided token and sends to server
    proof = client_zk.sign(usr1_credentials, token).dump()

    replayproof_usr1 = proof

    # Get the token from the client
    proof = ZKData.load(proof)
    token = ZKData.load(proof.data, ":")

    #Verify Proof
    if not server_zk.verify(token, server_signature):
        print("False")
    else:
        print(client_zk.verify(proof, client_signature, data=token))

    #1.1 Incorrect proof

    # Create a signed token and send to the client
    token = server_zk.sign("SecureServerPassword", client_zk.token())
    token = token.dump(separator=":")

    # Create a proof that signs the provided token and sends to server
    proof = client_zk.sign(usr2_credentials, token).dump()

    # Get the token from the client
    proof = ZKData.load(proof)
    token = ZKData.load(proof.data, ":")

    # In this example, the server signs the token so it can be sure it has not been modified
    if not server_zk.verify(token, server_signature):
        print("False")
    else:
        print(client_zk.verify(proof, client_signature, data=token))


    ### 2. Soundness: Replay attack failure ###


    ##2. usr2 trying to impersonate with usr1's proof ##

    # Create signature and send to server
    signature = client_zk.create_signature(usr2_credentials)

    # Load the received signature from the Client
    sig = signature.dump()
    client_signature = ZKSignature.load(sig)
    client_zk = ZK(client_signature.params)

    # we assume that this is a reattempt to login, so server would generate a new token
    # Create a signed token and send to the client
    token = server_zk.sign("SecureServerPassword", client_zk.token())
    token = token.dump(separator=":")


    # Malicious proof intercepted from usr1
    proof = ZKData.load(replayproof_usr1)
    token = ZKData.load(proof.data, ":")    

    # In this example, the server signs the token so it can be sure it has not been modified
    if not server_zk.verify(token, server_signature):
        print("False")
    else:
        print(client_zk.verify(proof, client_signature, data=token))




if __name__ == "__main__":
    main()