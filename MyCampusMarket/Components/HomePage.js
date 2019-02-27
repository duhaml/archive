import React from 'react'
import { StyleSheet, View, TextInput, Button, Text } from 'react-native'

class HomePage extends React.Component {
  render() {
    return (
      <View style={styles.main_container}>
        <View style={styles.intro}>
            //image logo flex 2
            <Text style={styles.titleText}>MyCampusMarket</Text>{'\n'}{'\n'}
            <Text style={styles.baseText}>Bienvenue et tout, tu vas voir c'est cool par ici</Text>
        </View>
        <View style={styles.boutons}>
          <Button title='Créer un compte !' onPress={() => {this.props.navigation.navigate("CreateAccount")}} style={styles.buttons}/>
          <Button title='Déjà inscrit ?' onPress={() => {this.props.navigation.navigate("Login")}} style={styles.buttons}/>
        <View style={styles.cguContainer}>
          <Text onPress={() => {this.props.navigation.navigate("CGU")}} style={styles.cgu}>CGU</Text>
          <Text style={flex: 3}>a</Text>
          <Text onPress={() => {this.props.navigation.navigate("APropos")}} style={styles.cgu}>à propos</Text>
        </View>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  main_container: {
    flex: 1,
    marginTop: 20,
    backgroundColor: 'steelblue'
  },
  intro: {
    flex: 2,
  },
  baseText: {
    flex: 3,
    marginTop: 20,
    fontFamily: 'sans-serif',
    textAlign: 'center',
  },
  titleText: {
    flex: 3,
    marginTop: 20,
    fontSize: 20,
    fontWeight: 'bold',
  },
  boutons: {
    flex: 3,
    //align horiz
  },
  buttons: {
    flex: 2,
    marginTop: 0,
    borderRadius: 200,
    marginLeft:20,
    marginRight:20,
    alignItems: 'center',
  },
  cguContainer: {
    flex: 3,
    //align horiz
  },
  cgu: {
    flex: 3,
    textDecorationLine: 'underline',
  },
})

export default HomePage
